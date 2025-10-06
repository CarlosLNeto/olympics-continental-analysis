#!/usr/bin/env python3
"""
Script para criar gráficos de PARTICIPAÇÃO de países nas Olimpíadas
(todos os países que participaram, não apenas os que ganharam medalhas)
"""

import pandas as pd
import matplotlib.pyplot as plt
from pathlib import Path
import sys

# Adicionar path para importar funções
sys.path.insert(0, str(Path.cwd() / 'code' / 'parte2'))
from noc_to_continent import get_continent

# Cores padrão para continentes
CONTINENT_COLORS = {
    'Europa': '#4472C4',
    'Américas': '#ED7D31',
    'Ásia': '#FFC000',
    'África': '#70AD47',
    'Oceania': '#9966CC',
    'Diversos': '#A5A5A5'
}

def get_continent_color(continent):
    return CONTINENT_COLORS.get(continent, '#808080')

# Paths
BASE_PATH = Path.cwd()
RAW_PATH = BASE_PATH / 'raw'
OUTPUTS_PATH = BASE_PATH / 'outputs'
GOLD_PATH = BASE_PATH / 'gold' / 'parte2'

# Criar diretórios se não existirem
(OUTPUTS_PATH / 'figures').mkdir(parents=True, exist_ok=True)
GOLD_PATH.mkdir(parents=True, exist_ok=True)

print('='*80)
print('CRIANDO GRÁFICOS DE PARTICIPAÇÃO (TODOS OS PAÍSES)')
print('='*80)

# ===== CARREGAR DADOS DE PARTICIPANTES (NÃO APENAS MEDALHISTAS) =====
print('\n📂 Carregando dados de participantes...')

# Dados históricos - TODOS os resultados (não apenas medalhas)
df_results = pd.read_csv(RAW_PATH / 'Olympics_1896_2022' / 'world_olympedia_olympics_athlete_event_result.csv')
df_games = pd.read_csv(RAW_PATH / 'Olympics_1896_2022' / 'world_olympedia_olympics_game.csv')

print(f'✅ {len(df_results):,} resultados históricos carregados')
print(f'✅ {len(df_games):,} jogos carregados')

# ===== PREPARAR DADOS =====
print('\n🔧 Preparando dados...')

# Merge com jogos para obter ano e temporada
df_games_prep = df_games[['edition_id', 'year', 'edition']].copy()
df_games_prep['game_season'] = df_games_prep['edition'].apply(
    lambda x: 'Summer' if 'Summer' in str(x) else 'Winter'
)
df_games_prep = df_games_prep.rename(columns={'year': 'game_year'})

# Merge
df = df_results.merge(df_games_prep[['edition_id', 'game_year', 'game_season']], 
                      on='edition_id', how='left')

# Adicionar continente
df['continent'] = df['country_noc'].apply(get_continent)

# Remover continente desconhecido
df = df[df['continent'] != 'Desconhecido']

# Adicionar Paris 2024
print('\n📂 Adicionando dados de Paris 2024...')
df_paris = pd.read_csv(RAW_PATH / 'Olympics_Paris2024' / 'athletes.csv')
df_paris['game_year'] = 2024
df_paris['game_season'] = 'Summer'
df_paris['continent'] = df_paris['country_code'].apply(get_continent)
df_paris = df_paris.rename(columns={'country_code': 'country_noc'})
df_paris = df_paris[df_paris['continent'] != 'Desconhecido']

print(f'✅ {len(df):,} participações históricas')
print(f'✅ {len(df_paris):,} atletas Paris 2024')

# ===== SEPARAR POR TEMPORADA =====
df_summer = df[df['game_season'] == 'Summer']
df_winter = df[df['game_season'] == 'Winter']

# Adicionar Paris aos jogos de verão
df_summer_total = pd.concat([
    df_summer[['game_year', 'continent', 'country_noc']],
    df_paris[['game_year', 'continent', 'country_noc']]
], ignore_index=True)

print(f'\n📊 Jogos de Verão: {df_summer_total["game_year"].nunique()} edições')
print(f'📊 Jogos de Inverno: {df_winter["game_year"].nunique()} edições')

# ===== CALCULAR PAÍSES POR ANO =====
print('\n📈 Calculando países participantes por ano...')

# VERÃO
countries_year_summer = df_summer_total.groupby(['game_year', 'continent'])['country_noc'].nunique().unstack(fill_value=0)

# INVERNO  
countries_year_winter = df_winter.groupby(['game_year', 'continent'])['country_noc'].nunique().unstack(fill_value=0)

# Estatísticas
stats_summer = countries_year_summer.agg(['mean', 'std', 'min', 'max'])
stats_winter = countries_year_winter.agg(['mean', 'std', 'min', 'max'])

print('\n📊 ESTATÍSTICAS - JOGOS DE VERÃO (países participantes):')
for cont in stats_summer.columns:
    print(f'{cont:12}: média={stats_summer.loc["mean", cont]:.1f}, '
          f'std={stats_summer.loc["std", cont]:.1f}, '
          f'min={stats_summer.loc["min", cont]:.0f}, '
          f'max={stats_summer.loc["max", cont]:.0f}')

print('\n📊 ESTATÍSTICAS - JOGOS DE INVERNO (países participantes):')
for cont in stats_winter.columns:
    print(f'{cont:12}: média={stats_winter.loc["mean", cont]:.1f}, '
          f'std={stats_winter.loc["std", cont]:.1f}, '
          f'min={stats_winter.loc["min", cont]:.0f}, '
          f'max={stats_winter.loc["max", cont]:.0f}')

# ===== CRIAR GRÁFICOS =====
print('\n🎨 Criando gráficos...')

fig, axes = plt.subplots(1, 2, figsize=(20, 8))

# ===== GRÁFICO DE VERÃO =====
for cont in countries_year_summer.columns:
    axes[0].plot(countries_year_summer.index, countries_year_summer[cont],
                marker='o',
                label=f'{cont} (média: {stats_summer.loc["mean", cont]:.1f})',
                linewidth=2,
                color=get_continent_color(cont))

axes[0].set_xlabel('Ano', fontsize=12)
axes[0].set_ylabel('Número de Países Participantes', fontsize=12)
axes[0].set_title('Participação por Continente - Jogos de Verão (1896-2024)\n(Todos os países participantes)', 
                 fontsize=14, fontweight='bold')
axes[0].legend(fontsize=9, loc='upper left')
axes[0].grid(True, alpha=0.3)

# Nota explicativa
axes[0].text(0.5, 0.02, 
            'Nota: Este gráfico mostra TODOS os países que participaram, não apenas os que ganharam medalhas',
            transform=axes[0].transAxes, ha='center', fontsize=9,
            bbox=dict(boxstyle='round,pad=0.5', facecolor='lightyellow', alpha=0.8))

# ===== GRÁFICO DE INVERNO =====
for cont in countries_year_winter.columns:
    axes[1].plot(countries_year_winter.index, countries_year_winter[cont],
                marker='o',
                label=f'{cont} (média: {stats_winter.loc["mean", cont]:.1f})',
                linewidth=2,
                color=get_continent_color(cont))

axes[1].set_xlabel('Ano', fontsize=12)
axes[1].set_ylabel('Número de Países Participantes', fontsize=12)
axes[1].set_title('Participação por Continente - Jogos de Inverno (1924-2022)\n(Todos os países participantes)', 
                 fontsize=14, fontweight='bold')
axes[1].legend(fontsize=9, loc='upper left')
axes[1].grid(True, alpha=0.3)

# Nota explicativa para Américas no inverno
if 'Américas' in countries_year_winter.columns:
    americas_data = countries_year_winter['Américas']
    if (americas_data > 0).any():
        # Mostrar quantos países das Américas nos últimos jogos
        last_year = americas_data[americas_data > 0].index[-1]
        last_count = int(americas_data[last_year])
        axes[1].text(last_year, americas_data[last_year] + 0.5,
                    f'{last_count} países\ndas Américas\n(incluindo Brasil!)',
                    fontsize=8, ha='center',
                    bbox=dict(boxstyle='round,pad=0.3', facecolor='white', 
                             edgecolor='orange', alpha=0.9))

axes[1].text(0.5, 0.02,
            'Nota: Este gráfico mostra TODOS os países participantes. Brasil participa desde 1992!',
            transform=axes[1].transAxes, ha='center', fontsize=9,
            bbox=dict(boxstyle='round,pad=0.5', facecolor='lightyellow', alpha=0.8))

plt.tight_layout()
plt.savefig(OUTPUTS_PATH / 'figures' / 'parte2_participacao_todos_paises.png', 
           dpi=300, bbox_inches='tight')
print(f'\n💾 Gráfico salvo: parte2_participacao_todos_paises.png')
plt.show()

# ===== SALVAR DADOS =====
countries_year_summer.to_parquet(GOLD_PATH / 'participacao_todos_paises_summer.parquet')
countries_year_winter.to_parquet(GOLD_PATH / 'participacao_todos_paises_winter.parquet')
stats_summer.to_parquet(GOLD_PATH / 'participacao_todos_paises_stats_summer.parquet')
stats_winter.to_parquet(GOLD_PATH / 'participacao_todos_paises_stats_winter.parquet')

print('💾 Dados salvos:')
print('   - participacao_todos_paises_summer.parquet')
print('   - participacao_todos_paises_winter.parquet')
print('   - participacao_todos_paises_stats_summer.parquet')
print('   - participacao_todos_paises_stats_winter.parquet')

# ===== COMPARAÇÃO: PARTICIPANTES vs MEDALHISTAS =====
print('\n' + '='*80)
print('📊 COMPARAÇÃO: Jogos de Inverno - Américas')
print('='*80)

# Carregar dados de medalhistas (gráfico anterior)
try:
    medals_winter = pd.read_parquet(GOLD_PATH / 'crescimento_temporal_winter.parquet')
    
    print('\nÚltimos 5 Jogos de Inverno - AMÉRICAS:')
    print('\n' + '-'*60)
    print(f'{"Ano":>6} | {"Países Participantes":>20} | {"Países Medalhistas":>20}')
    print('-'*60)
    
    last_5_years = sorted(countries_year_winter.index)[-5:]
    for year in last_5_years:
        part = int(countries_year_winter.loc[year, 'Américas']) if 'Américas' in countries_year_winter.columns else 0
        medal = int(medals_winter.loc[year, 'Américas']) if year in medals_winter.index and 'Américas' in medals_winter.columns else 0
        print(f'{year:>6} | {part:>20} | {medal:>20}')
    
    print('-'*60)
    print('\n💡 INSIGHT: Vários países das Américas participam mas não ganham medalhas!')
    print('   Brasil está entre os participantes mas não entre os medalhistas.')
    
except Exception as e:
    print(f'⚠️  Não foi possível carregar dados de medalhistas: {e}')

print('\n✅ CONCLUÍDO!')
print('='*80)
