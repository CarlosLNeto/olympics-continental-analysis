# 📋 Instruções de Execução

## Pré-requisitos

- Python 3.8 ou superior
- pip (gerenciador de pacotes Python)
- Git
- ~500MB de espaço em disco

## Instalação Passo a Passo

### 1. Preparar o Ambiente

```bash
# Navegar até a pasta do projeto
cd AnalisesPorContinente

# Criar ambiente virtual (opcional mas recomendado)
python -m venv venv

# Ativar o ambiente virtual
# No macOS/Linux:
source venv/bin/activate
# No Windows:
venv\Scripts\activate
```

### 2. Instalar Dependências

```bash
pip install -r requirements.txt
```

Isso instalará:
- pandas (manipulação de dados)
- numpy (operações numéricas)
- matplotlib (gráficos)
- seaborn (visualizações estatísticas)
- pyarrow (suporte a Parquet)
- jupyter (notebooks interativos)

### 3. Iniciar Jupyter Notebook

```bash
jupyter notebook
```

Isso abrirá o Jupyter no seu navegador.

## Ordem de Execução dos Notebooks

### Notebook 1: Processamento Bronze Layer
📁 `notebooks/01_bronze_layer_processing.ipynb`

**O que faz:**
- Lê os arquivos CSV da pasta `raw/`
- Converte para formato Parquet (mais eficiente)
- Cria metadados JSON para cada arquivo
- Salva tudo na pasta `bronze/`

**Tempo estimado:** 2-3 minutos

**Como executar:**
1. Abra o notebook
2. Clique em "Cell" → "Run All"
3. Aguarde a conclusão

**Saídas esperadas:**
- 9 arquivos `.parquet` em `bronze/`
- 9 arquivos `*_metadata.json` em `bronze/`

---

### Notebook 2: Parte 1 - Consolidação de Medalhas
📁 `notebooks/02_part1_medals_consolidation.ipynb`

**O que faz:**
- Consolida medalhas por país
- Separa Jogos de Verão, Inverno e Total Geral
- Cria rankings dos top 50 países
- Gera gráficos de barras horizontais

**Tempo estimado:** 1-2 minutos

**Como executar:**
1. Abra o notebook
2. Execute "Cell" → "Run All"

**Saídas esperadas:**
- 3 arquivos `.parquet` em `gold/`
- 3 arquivos `.csv` em `outputs/tables/`
- 3 gráficos `.png` em `outputs/figures/`:
  - `top50_medals_summer.png`
  - `top50_medals_winter.png`
  - `top50_medals_total.png`

**Resultados principais:**
- Top 3 países em Total Geral
- Rankings oficiais de medalhas

---

### Notebook 3a: Parte 2 - Análise por Continente (Q1)
📁 `notebooks/03a_part2_continent_analysis_q1.ipynb`

**O que faz:**
- Cria mapeamento de países para continentes
- Integra dados de medalhas com continentes
- Responde à pergunta 2.1:
  - Distribuição total por continente
  - Medalhas por edição
  - Número médio de atletas

**Tempo estimado:** 2-3 minutos

**Como executar:**
1. Abra o notebook
2. Execute "Cell" → "Run All"

**Saídas esperadas:**
- Arquivos em `bronze/`:
  - `noc_continent_mapping.parquet`
  - `medals_by_continent.parquet`
  - `athletes_by_continent.parquet`
- Arquivos em `gold/`:
  - `medals_by_continent_total.parquet`
  - `medals_by_year_continent.parquet`
  - `avg_athletes_by_continent.parquet`
- Gráficos em `outputs/figures/`:
  - `medals_by_continent_pie.png`
  - `medals_by_year_continent_line.png`

---

### Notebook 3b: Parte 2 - Análise por Continente (Q2-5)
📁 `notebooks/03b_part2_continent_analysis_q2-5.ipynb`

**O que faz:**
- Responde às perguntas 2.2 a 2.5:
  - 2.2: Crescimento da representação
  - 2.3: Participação feminina
  - 2.4: Modalidades mais fortes
  - 2.5: Crescimento 1986-2024

**Tempo estimado:** 2-3 minutos

**Como executar:**
1. Abra o notebook
2. Execute "Cell" → "Run All"

**Saídas esperadas:**
- Arquivos em `gold/`:
  - `representation_stats_by_continent.parquet`
  - `female_participation_by_continent.parquet`
  - `top_sports_by_continent.parquet`
  - `medals_growth_1986_2024.parquet`
- Gráficos em `outputs/figures/`:
  - `athletes_growth_by_continent.png`
  - `female_participation_evolution.png`
  - `female_participation_recent.png`
  - `top_sports_by_continent.png`
  - `medals_growth_comparison.png`
  - `medals_evolution_1986_2022.png`

---

## Estrutura de Pastas Após Execução

```
AnalisesPorContinente/
├── raw/                     # Dados originais (já existentes)
├── bronze/                  # ✅ 15+ arquivos criados
├── gold/                    # ✅ 10+ arquivos criados
├── outputs/
│   ├── tables/             # ✅ 10+ arquivos CSV
│   └── figures/            # ✅ 12+ gráficos PNG
└── notebooks/              # 4 notebooks executados
```

## Solução de Problemas

### Erro: "Module not found"
```bash
pip install -r requirements.txt
```

### Erro: "File not found" ao executar notebooks
- Certifique-se de estar na pasta raiz do projeto
- Verifique se executou os notebooks na ordem correta

### Erro: "Memory error" ao processar athlete_bio
- Esse arquivo é grande (~50MB)
- Feche outros programas para liberar memória
- O Parquet usa compressão, então após conversão será menor

### Gráficos não aparecem
- Adicione `%matplotlib inline` no topo do notebook
- Ou use `plt.show()` após cada gráfico

### Jupyter não abre
```bash
# Reinstalar Jupyter
pip install --upgrade jupyter notebook
jupyter notebook
```

## Verificação de Sucesso

Após executar todos os notebooks, você deve ter:

1. ✅ **Bronze Layer**: 15+ arquivos Parquet
2. ✅ **Gold Layer**: 10+ arquivos Parquet  
3. ✅ **Tabelas**: 10+ arquivos CSV
4. ✅ **Gráficos**: 12+ imagens PNG
5. ✅ **Metadados**: JSON para cada dataset

## Tempo Total Estimado

- Instalação: 5 minutos
- Execução de todos os notebooks: 8-12 minutos
- **Total: ~15-20 minutos**

## Próximos Passos

Após executar tudo:
1. Explorar os gráficos em `outputs/figures/`
2. Analisar as tabelas em `outputs/tables/`
3. Revisar insights nos notebooks
4. Personalizar análises conforme necessário

## Suporte

Para dúvidas ou problemas:
1. Verifique a documentação do Python/Pandas
2. Consulte os comentários nos notebooks
3. Revise os metadados JSON gerados

## Dicas de Performance

- Execute um notebook de cada vez se tiver pouca memória
- O primeiro notebook demora mais (conversão para Parquet)
- Gráficos complexos podem levar alguns segundos

---

✅ **Pronto!** Agora você tem uma análise completa das Olimpíadas por continente!
