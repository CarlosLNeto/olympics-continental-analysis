# 🏅 Análise de Medalhas Olímpicas por País (1896-2024)

[![Python](https://img.shields.io/badge/Python-3.8+-blue.svg)](https://www.python.org/)
[![Pandas](https://img.shields.io/badge/Pandas-1.5+-green.svg)](https://pandas.pydata.org/)
[![License](https://img.shields.io/badge/License-Educational-orange.svg)](LICENSE)
[![Status](https://img.shields.io/badge/Status-Completo-success.svg)](README.md)

Análise completa de medalhas olímpicas por país desde 1896 até 2024, incluindo dados históricos (Olympedia) e das Olimpíadas de Paris 2024. O projeto implementa uma arquitetura de **Data Lake** simplificada com integração de dados de múltiplas fontes e visualizações profissionais dos resultados.

## ✅ Status do Projeto

**✨ Projeto COMPLETO e FUNCIONAL! ✨**

- ✅ **Integração de Dados**: Combinação de dados históricos (1896-2022) + Paris 2024
- ✅ **Processamento ETL**: Pipeline Data Lake com camadas Raw → Bronze → Gold
- ✅ **Análise Consolidada**: Medalhas por país em Jogos de Verão, Inverno e Total Geral
- ✅ **Visualizações**: Gráficos profissionais dos Top 50 países com destaque para Brasil e Cuba
- ✅ **Formato Eficiente**: Armazenamento em Parquet com metadados JSON
- ✅ **Notebook Interativo**: Análise completa com resultados salvos e reproduzíveis

## 📊 Datasets

### Olympics 1896-2022 (Olympedia)
Dados históricos completos das Olimpíadas:
- **135K+ atletas** com informações biográficas
- **270K+ resultados** de eventos
- **5.5K+ registros** de medalhas por país/edição
- **230+ países** participantes
- **Cobertura**: Jogos de Verão e Inverno desde 1896

### Olympics Paris 2024
Dados oficiais das Olimpíadas mais recentes:
- **11K+ atletas** participantes
- **329 eventos** em 45 modalidades
- **2K+ medalhas** distribuídas
- Resultados detalhados por modalidade

## 🎯 Análises Realizadas

### 📊 Consolidação de Medalhas por País (1896-2024)

> **✨ Dados Completos:** Integração de dados históricos (1896-2022) + Paris 2024

**Três análises completas com rankings oficiais:**

1. **🌞 Medalhas - Jogos de Verão** (160 países com medalhas)
   - Ranking consolidado de todas as edições incluindo Paris 2024
   - Gráfico Top 50 com distribuição Ouro/Prata/Bronze
   - Brasil e Cuba sempre visíveis com destaque

2. **❄️ Medalhas - Jogos de Inverno** (47 países com medalhas)
   - Ranking consolidado de todas as edições de inverno
   - Gráfico Top 50 mostrando domínio de países do hemisfério norte
   - Análise focada em países com tradição em esportes de inverno

3. **🏆 Medalhas - Total Geral** (Verão + Inverno) (161 países)
   - Ranking combinado definitivo de 1896 a 2024
   - Visão completa do desempenho olímpico histórico
   - Top 50 países no pódio olímpico mundial

**Características das Análises:**
- ✅ Dados integrados de 1896 até Paris 2024 (128 anos de história olímpica)
- ✅ Rankings baseados nas fontes oficiais (Olympedia + Olympics.com)
- ✅ Visualizações profissionais com paleta de cores ouro/prata/bronze
- ✅ Tabelas exportadas em CSV para uso em apresentações
- ✅ Gráficos em alta resolução (PNG) para relatórios

## 🏗️ Arquitetura do Projeto

```
AnalisesPorContinente/
│
├── 📁 raw/                           # Camada Raw - Dados originais
│   ├── Olympics_1896_2022/           # Dados históricos Olympedia
│   │   ├── world_olympedia_olympics_athlete_bio.csv
│   │   ├── world_olympedia_olympics_athlete_event_result.csv
│   │   ├── world_olympedia_olympics_country.csv
│   │   ├── world_olympedia_olympics_game.csv
│   │   ├── world_olympedia_olympics_game_medal_tally.csv
│   │   ├── world_olympedia_olympics_result.csv
│   │   └── metadata.json
│   │
│   └── Olympics_Paris2024/           # Dados Paris 2024
│       ├── athletes.csv
│       ├── medallists.csv
│       ├── medals.csv
│       ├── medals_total.csv
│       ├── results/                  # 45 modalidades
│       └── metadata.json
│
├── 📁 bronze/                        # Camada Bronze - Dados integrados
│   └── medals_integrated_1896_2024.parquet  # Medalhas consolidadas
│
├── 📁 gold/                          # Camada Gold - Dados analíticos
│   ├── medals_summer.parquet         # Análise Jogos de Verão
│   ├── medals_summer_metadata.json
│   ├── medals_winter.parquet         # Análise Jogos de Inverno
│   ├── medals_winter_metadata.json
│   ├── medals_total.parquet          # Análise Total Geral
│   └── medals_total_metadata.json
│
├── 📁 notebooks/                     # Jupyter Notebooks
│   ├── analise_medalhas.ipynb        # 🎯 NOTEBOOK PRINCIPAL
│   └── check_parquet.py              # Utilitário para validar parquet
│
├── 📁 outputs/                       # Outputs para apresentação
│   ├── figures/                      # Visualizações
│   │   ├── top50_summer.png          # Top 50 Jogos de Verão
│   │   ├── top50_winter.png          # Top 50 Jogos de Inverno
│   │   └── top50_total.png           # Top 50 Total Geral
│   │
│   └── tables/                       # Tabelas exportadas
│       ├── medals_summer.csv         # Ranking Jogos de Verão
│       ├── medals_winter.csv         # Ranking Jogos de Inverno
│       └── medals_total.csv          # Ranking Total Geral
│
├── 📁 src/                           # Scripts auxiliares (futuro)
│
├── 📄 requirements.txt               # Dependências Python
├── 📄 .gitignore                     # Arquivos ignorados pelo Git
└── 📄 README.md                      # Este arquivo
```

## 🚀 Como Usar

### 📖 Opção 1: Visualizar Resultados (Recomendado)

**O notebook já contém todos os resultados executados!** Basta abrir e explorar:

```bash
# Abrir Jupyter Notebook
jupyter notebook

# Navegue até: notebooks/analise_medalhas.ipynb
```

**Você também pode visualizar diretamente os outputs:**
- 📊 **Gráficos**: Abra os arquivos PNG em `outputs/figures/`
- 📋 **Tabelas**: Abra os arquivos CSV em `outputs/tables/` (Excel, LibreOffice, Google Sheets)
- 💾 **Dados processados**: Arquivos Parquet em `gold/` (pandas, DuckDB, Spark)

### 🔄 Opção 2: Re-executar Análises

Se desejar executar o pipeline completo do zero:

```bash
# 1. Clone o repositório (se ainda não tiver)
git clone <url-do-repositorio>
cd AnalisesPorContinente

# 2. Instalar dependências
pip install -r requirements.txt

# 3. Abrir Jupyter
jupyter notebook

# 4. Execute: notebooks/analise_medalhas.ipynb
#    Menu: Cell > Run All
```

**⏱️ Tempo estimado:** 2-5 minutos

### ⚙️ Pré-requisitos

- **Python**: 3.8 ou superior (Python 3.11+ recomendado)
- **Espaço em disco**: ~500MB
- **RAM**: 2GB recomendado
- **Sistema**: Windows, macOS ou Linux

**Dependências principais:**
- pandas, numpy (manipulação de dados)
- matplotlib, seaborn (visualizações)
- pyarrow (suporte Parquet)
- jupyter (notebooks interativos)

## 📈 Resultados Principais

### 🏆 Top 3 Países - Ranking Total Geral (1896-2024)

| Pos | País | Código | 🥇 Ouro | 🥈 Prata | 🥉 Bronze | Total |
|-----|------|--------|----------|-----------|-----------|--------|
| 1º  | Estados Unidos | USA | 1,235 | 1,013 | 887 | **3,135** |
| 2º  | União Soviética | URS | 473 | 376 | 355 | **1,204** |
| 3º  | Alemanha | GER | 367 | 390 | 374 | **1,131** |

### 🌎 Destaque: Brasil e Cuba

| País | Ranking | 🥇 Ouro | 🥈 Prata | 🥉 Bronze | Total |
|------|---------|----------|-----------|-----------|--------|
| 🇧🇷 **Brasil** | **30º** | 40 | 49 | 81 | **170** |
| 🇨🇺 **Cuba** | **23º** | 86 | 70 | 88 | **244** |

> 💡 **Incluindo Paris 2024:** Brasil conquistou 20 medalhas (3🥇 7🥈 10🥉) em Paris 2024!

### 📊 Visualizações Disponíveis

Todos os resultados estão salvos e prontos para uso:

**🖼️ Gráficos (PNG - Alta Resolução):**
- `outputs/figures/top50_summer.png` - Top 50 países em Jogos de Verão
- `outputs/figures/top50_winter.png` - Top 50 países em Jogos de Inverno
- `outputs/figures/top50_total.png` - Top 50 países no Total Geral

**📋 Tabelas (CSV - Prontas para Excel):**
- `outputs/tables/medals_summer.csv` - Ranking completo Jogos de Verão
- `outputs/tables/medals_winter.csv` - Ranking completo Jogos de Inverno
- `outputs/tables/medals_total.csv` - Ranking completo Total Geral

**💾 Dados Processados (Parquet - Para análises):**
- `gold/medals_summer.parquet` + metadados
- `gold/medals_winter.parquet` + metadados
- `gold/medals_total.parquet` + metadados

## 🛠️ Tecnologias Utilizadas

- **Python 3.8+**
- **Pandas** - Manipulação de dados
- **NumPy** - Operações numéricas
- **Matplotlib & Seaborn** - Visualizações
- **PyArrow** - Suporte a Parquet
- **Jupyter** - Notebooks interativos

## 📝 Metadados

Cada arquivo Parquet possui um arquivo JSON de metadados com:
- Nome do dataset
- Descrição
- Data de criação
- Fonte dos dados
- Dimensões (linhas/colunas)
- Lista de colunas
- Tipos de dados
- Valores faltantes

## 🔍 Insights e Descobertas

### 🌍 Análise Geopolítica

1. **Domínio Norte-Americano**: EUA lidera com mais que o dobro de medalhas do 2º colocado
2. **Legado Soviético**: União Soviética mantém 2º lugar mesmo após dissolução (1991)
3. **Potência Alemã**: Alemanha unificada e suas variações históricas somam 1,098 medalhas
4. **Europa Dominante**: 7 dos Top 10 países são europeus
5. **Tradição Esportiva**: Países com investimento histórico em esporte mantêm posições de destaque

### 🌞 Jogos de Verão vs ❄️ Jogos de Inverno

- **Verão**: 54 países com medalhas / maior diversidade geográfica
- **Inverno**: 25 países com medalhas / concentração no hemisfério norte
- **Diferença**: Jogos de Verão têm ~3x mais medalhas distribuídas

### 🇧🇷 Brasil - Análise Detalhada

- **Posição Global**: 30º lugar
- **Total de Medalhas**: 170 (40🥇 49🥈 81🥉)
- **Paris 2024**: 20 medalhas (3🥇 7🥈 10🥉) - Melhor campanha em medalhas totais
- **Forte em**: Futebol, vôlei, judô, vela, atletismo, ginástica
- **Tendência**: Crescimento consistente desde 1988 (Seul)

### 🇨🇺 Cuba - Análise Detalhada

- **Posição Global**: 23º lugar
- **Total de Medalhas**: 244 (86🥇 70🥈 88🥉)
- **Forte em**: Boxe, atletismo, luta, judô, vôlei
- **Tradição**: Potência esportiva latino-americana
- **Destaques**: Alto índice de medalhas de ouro (35.2%)

## 📚 Fontes dos Dados

- **Base dos Dados** - Dados históricos 1896-2022
  - https://basedosdados.org/dataset/62f8cb83-ac37-48be-874b-b94dd92d3e2b
- **Kaggle** - Paris 2024 Olympic Summer Games
  - https://www.kaggle.com/datasets/piterfm/paris-2024-olympic-summer-games/data

## 🤝 Contribuições

Este é um projeto educacional. Sugestões e melhorias são bem-vindas!

## 📄 Licença

Este projeto é para fins educacionais e de análise de dados.

## 👥 Autores

**Carlos Lavor Neto**  
Engenharia de Computação - UEA  
Ciência de Dados

**Alexandro Pantoja**  
Engenharia de Computação - UEA  
Ciência de Dados

---

⭐ Se este projeto foi útil, considere dar uma estrela no repositório!
