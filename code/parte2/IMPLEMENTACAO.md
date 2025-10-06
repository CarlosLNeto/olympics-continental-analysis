# 📋 Guia de Implementação - Parte 2

## ✅ O que já está pronto:

1. **Estrutura do notebook** (`parte2_analise_continentes.ipynb`)
   - Seções organizadas (2.1 a 2.5)
   - Importações configuradas
   - Paths definidos

2. **Mapeamento NOC → Continente** (`noc_to_continent.py`)
   - 221 códigos NOC mapeados
   - 5 continentes + códigos históricos
   - Funções auxiliares

3. **Dados brutos** (`raw/` compartilhado)
   - Olympics 1896-2022
   - Paris 2024

## 🚧 O que precisa ser implementado:

### Passo 1: Carregar e Integrar Dados

```python
# Carregar dados históricos
df_hist_results = pd.read_csv(RAW_PATH / 'Olympics_1896_2022' / 'world_olympedia_olympics_athlete_event_result.csv')
df_hist_athletes = pd.read_csv(RAW_PATH / 'Olympics_1896_2022' / 'world_olympedia_olympics_athlete_bio.csv')
df_hist_countries = pd.read_csv(RAW_PATH / 'Olympics_1896_2022' / 'world_olympedia_olympics_country.csv')
df_hist_games = pd.read_csv(RAW_PATH / 'Olympics_1896_2022' / 'world_olympedia_olympics_game.csv')

# Carregar Paris 2024
df_paris_athletes = pd.read_csv(RAW_PATH / 'Olympics_Paris2024' / 'athletes.csv')
df_paris_medallists = pd.read_csv(RAW_PATH / 'Olympics_Paris2024' / 'medallists.csv')

# Importar mapeamento
from noc_to_continent import get_continent

# Integrar e adicionar continente
df_medals = ... # Filtrar medalhas
df_medals['continent'] = df_medals['country_noc'].apply(get_continent)

# Salvar em Bronze
df_medals.to_parquet(BRONZE_PATH / 'medals_integrated.parquet', index=False)
```

### Passo 2: Análise 2.1 - Distribuição de Medalhas

```python
# Total por continente
medals_by_continent = df_medals.groupby('continent')['medal'].count()

# Gráfico de Pizza
plt.figure(figsize=(10, 10))
plt.pie(medals_by_continent.values, labels=medals_by_continent.index, 
        autopct='%1.1f%%', startangle=90)
plt.title('Distribuição Total de Medalhas por Continente (1896-2024)')
plt.savefig(OUTPUTS_PATH / 'figures' / 'medals_pie_continente.png', dpi=300, bbox_inches='tight')

# Evolução temporal
medals_by_year = df_medals.groupby(['game_year', 'continent']).size().unstack(fill_value=0)

plt.figure(figsize=(16, 8))
for continent in medals_by_year.columns:
    plt.plot(medals_by_year.index, medals_by_year[continent], marker='o', label=continent)
plt.xlabel('Ano')
plt.ylabel('Número de Medalhas')
plt.title('Evolução de Medalhas por Continente ao Longo do Tempo')
plt.legend()
plt.grid(True, alpha=0.3)
plt.savefig(OUTPUTS_PATH / 'figures' / 'medals_evolucao_continente.png', dpi=300, bbox_inches='tight')

# Salvar resultado
medals_by_continent.to_frame('total_medalhas').to_parquet(GOLD_PATH / 'medals_por_continente.parquet')
```

### Passo 3: Análise 2.2 - Crescimento da Representação

```python
# Calcular crescimento por período
# Número de países participantes por continente ao longo do tempo
countries_by_year = df_medals.groupby(['game_year', 'continent'])['country_noc'].nunique().unstack(fill_value=0)

# Estatísticas
stats = countries_by_year.agg(['mean', 'std', 'min', 'max'])

# Gráfico de linha
plt.figure(figsize=(16, 8))
for continent in countries_by_year.columns:
    plt.plot(countries_by_year.index, countries_by_year[continent], 
             marker='o', label=f'{continent} (média: {stats.loc["mean", continent]:.1f})')
plt.xlabel('Ano')
plt.ylabel('Número de Países')
plt.title('Crescimento da Representação por Continente')
plt.legend()
plt.grid(True, alpha=0.3)
plt.savefig(OUTPUTS_PATH / 'figures' / 'crescimento_representacao.png', dpi=300, bbox_inches='tight')

# Salvar
stats.to_parquet(GOLD_PATH / 'crescimento_stats.parquet')
```

### Passo 4: Análise 2.3 - Participação Feminina

```python
# Filtrar dados de atletas com sexo conhecido
df_gender = df_medals[df_medals['athlete_sex'].notna()].copy()

# Calcular percentual feminino
gender_by_continent = df_gender.groupby(['game_year', 'continent', 'athlete_sex']).size().unstack(fill_value=0)
gender_pct = gender_by_continent.div(gender_by_continent.sum(axis=1), axis=0) * 100

# Extrair percentual feminino
female_pct = gender_pct.xs('F', axis=1, level=1) if 'F' in gender_by_continent.columns else pd.DataFrame()

# Gráfico
plt.figure(figsize=(16, 8))
for continent in female_pct.columns:
    plt.plot(female_pct.index.get_level_values(0), female_pct[continent], 
             marker='o', label=continent)
plt.xlabel('Ano')
plt.ylabel('% de Participação Feminina')
plt.title('Evolução da Participação Feminina por Continente')
plt.legend()
plt.grid(True, alpha=0.3)
plt.savefig(OUTPUTS_PATH / 'figures' / 'participacao_feminina.png', dpi=300, bbox_inches='tight')

# Salvar
female_pct.to_parquet(GOLD_PATH / 'participacao_feminina.parquet')
```

### Passo 5: Análise 2.4 - Modalidades Mais Fortes

```python
# Top 10 modalidades por continente
top_sports = {}
for continent in df_medals['continent'].unique():
    df_cont = df_medals[df_medals['continent'] == continent]
    top_10 = df_cont['event_discipline'].value_counts().head(10)
    top_sports[continent] = top_10

# Visualizar (exemplo para um continente)
fig, axes = plt.subplots(2, 3, figsize=(20, 12))
axes = axes.flatten()

for idx, (continent, sports) in enumerate(top_sports.items()):
    if idx < 6:
        sports.plot(kind='barh', ax=axes[idx])
        axes[idx].set_title(f'Top 10 Modalidades - {continent}')
        axes[idx].set_xlabel('Número de Medalhas')

plt.tight_layout()
plt.savefig(OUTPUTS_PATH / 'figures' / 'modalidades_continente.png', dpi=300, bbox_inches='tight')

# Salvar
pd.DataFrame(top_sports).to_parquet(GOLD_PATH / 'modalidades_fortes.parquet')
```

### Passo 6: Análise 2.5 - Crescimento 1896-2024

```python
# Comparar primeiro e último período
primeiro_periodo = df_medals[df_medals['game_year'] <= 1920]
ultimo_periodo = df_medals[df_medals['game_year'] >= 2000]

crescimento = pd.DataFrame({
    '1896-1920': primeiro_periodo.groupby('continent').size(),
    '2000-2024': ultimo_periodo.groupby('continent').size()
})
crescimento['crescimento_%'] = ((crescimento['2000-2024'] / crescimento['1896-1920']) - 1) * 100

# Gráfico
crescimento[['1896-1920', '2000-2024']].plot(kind='bar', figsize=(12, 6))
plt.title('Crescimento de Medalhas por Continente: 1896-1920 vs 2000-2024')
plt.ylabel('Número de Medalhas')
plt.xlabel('Continente')
plt.xticks(rotation=45)
plt.legend(['1896-1920', '2000-2024'])
plt.tight_layout()
plt.savefig(OUTPUTS_PATH / 'figures' / 'crescimento_1896_2024.png', dpi=300, bbox_inches='tight')

# Salvar
crescimento.to_parquet(GOLD_PATH / 'crescimento_temporal.parquet')
```

### Passo 7: Gerar Metadados

```python
# Para cada arquivo Parquet em gold/parte2/
metadata = {
    "nome": "Nome do Dataset",
    "descricao": "Descrição detalhada",
    "periodo": "1896-2024",
    "fonte": "Olympedia + Olympics.com",
    "criado_em": datetime.now().isoformat(),
    "colunas": list(df.columns),
    "total_registros": len(df)
}

with open(METADATA_PATH / 'arquivo_metadata.json', 'w') as f:
    json.dump(metadata, f, indent=2)
```

## 📊 Estrutura Final Esperada:

```
bronze/parte2/
└── medals_integrated.parquet

gold/parte2/
├── medals_por_continente.parquet
├── crescimento_stats.parquet
├── participacao_feminina.parquet
├── modalidades_fortes.parquet
└── crescimento_temporal.parquet

metadata/parte2/
├── medals_por_continente_metadata.json
├── crescimento_stats_metadata.json
├── participacao_feminina_metadata.json
├── modalidades_fortes_metadata.json
└── crescimento_temporal_metadata.json

outputs/figures/
├── medals_pie_continente.png
├── medals_evolucao_continente.png
├── crescimento_representacao.png
├── participacao_feminina.png
├── modalidades_continente.png
└── crescimento_1896_2024.png

outputs/tables/
├── medals_continente.csv
├── crescimento_stats.csv
└── ...
```

## 🚀 Como Executar:

1. Abra o notebook no Jupyter
2. Execute as células sequencialmente
3. Ajuste conforme necessário
4. Verifique os outputs gerados

## 💡 Dicas:

- Use `df.head()` para verificar dados
- Teste com subconjuntos pequenos primeiro
- Salve frequentemente
- Gere metadados para cada resultado
- Exporte tabelas importantes para CSV também
