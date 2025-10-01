# 🏅 Análise de Medalhas Olímpicas por País

[![Python](https://img.shields.io/badge/Python-3.8+-blue.svg)](https://www.python.org/)
[![Pandas](https://img.shields.io/badge/Pandas-1.5+-green.svg)](https://pandas.pydata.org/)
[![License](https://img.shields.io/badge/License-Educational-orange.svg)](LICENSE)
[![Status](https://img.shields.io/badge/Status-Completo-success.svg)](README.md)

Este repositório contém análise consolidada de medalhas olímpicas por país (1896-2024). O projeto implementa uma arquitetura de **Data Lake** com camadas Bronze e Gold, utilizando formato **Parquet** para armazenamento eficiente.

## ✅ Status do Projeto

**Projeto COMPLETO e FUNCIONAL!**

- ✅ Arquitetura Data Lake (Raw → Bronze → Gold)
- ✅ Processamento de 135K+ atletas e 270K+ resultados
- ✅ Consolidação de medalhas por país (Verão, Inverno, Total)
- ✅ Visualizações profissionais dos Top 50 países
- ✅ Documentação completa

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

### Consolidação de Medalhas por País (1896-2024)

**1.1 Tabelas Consolidadas:**
- ✅ Medalhas - Jogos de Verão (154 países)
- ✅ Medalhas - Jogos de Inverno (154 países)
- ✅ Medalhas - Total Geral (Verão + Inverno)
- ✅ Rankings oficiais compatíveis com Wikipedia

**1.2 Visualizações:**
- ✅ Top 50 países - Jogos de Verão
- ✅ Top 50 países - Jogos de Inverno
- ✅ Top 50 países - Total Geral
- ✅ Gráficos de barras horizontais empilhadas (Ouro/Prata/Bronze)

## 🏗️ Arquitetura Data Lake

```
AnalisesPorContinente/
├── raw/                              # Camada Raw - Dados originais
│   ├── Olympics_1896_2022/
│   │   ├── *.csv                     # Arquivos CSV originais
│   │   └── metadata.json             # Metadados do dataset
│   └── Olympics_Paris2024/
│       ├── *.csv
│       ├── results/*.csv             # 45 modalidades
│       └── metadata.json
│
├── bronze/                           # Camada Bronze - Dados limpos (✅ 9 arquivos)
│   ├── *.parquet                     # Dados em formato Parquet
│   ├── *_metadata.json               # Metadados de cada arquivo
│   ├── athlete_bio.parquet
│   ├── athlete_event_result.parquet
│   ├── athletes_paris2024.parquet
│   ├── country.parquet
│   ├── game.parquet
│   ├── medal_tally.parquet           # Principal para análises
│   ├── medals_paris2024.parquet
│   ├── medals_total_paris2024.parquet
│   └── result.parquet
│
├── gold/                             # Camada Gold - Dados analíticos (✅ 3 arquivos)
│   ├── medals_summer_consolidated.parquet (✅)
│   ├── medals_winter_consolidated.parquet (✅)
│   ├── medals_total_consolidated.parquet (✅)
│   └── *_metadata.json               # Metadados de cada análise
│
├── notebooks/                        # Jupyter Notebooks (✅ COM RESULTADOS!)
│   ├── 01_bronze_layer_processing.ipynb (✅)
│   └── 02_part1_medals_consolidation.ipynb (✅ ANÁLISE COMPLETA)
│
├── outputs/                          # Saídas para apresentação
│   ├── tables/                       # Tabelas em CSV (✅ 3 arquivos)
│   │   ├── medals_summer_consolidated.csv
│   │   ├── medals_winter_consolidated.csv
│   │   └── medals_total_consolidated.csv
│   └── figures/                      # Gráficos em PNG (✅ 3 imagens)
│       ├── top50_medals_summer.png
│       ├── top50_medals_winter.png
│       └── top50_medals_total.png
│
├── requirements.txt                  # Dependências Python
├── .gitignore                        # Arquivos ignorados pelo Git
├── CHANGELOG.md                      # Histórico de mudanças
└── README.md                         # Este arquivo
```

## 🚀 Como Usar

### Visualizar Resultados (Recomendado)

**O notebook já foi executado e contém todos os resultados!** Basta abrir para visualizar:

```bash
# Abrir Jupyter Notebook
jupyter notebook

# Navegue até notebooks/ e abra:
# - 02_part1_medals_consolidation.ipynb (TODOS os resultados da Parte 1)
```

Você também pode visualizar diretamente:
- **Gráficos**: Abra os arquivos PNG em `outputs/figures/`
- **Tabelas**: Abra os arquivos CSV em `outputs/tables/` com Excel ou Google Sheets

### Re-executar Análises (Opcional)

Se quiser re-executar as análises do zero:

```bash
# 1. Instalar dependências
pip install -r requirements.txt

# 2. Abrir Jupyter
jupyter notebook

# 3. Execute "Cell > Run All" em cada notebook, na ordem:
# - 01_bronze_layer_processing.ipynb (processa dados raw → bronze)
# - 02_part1_medals_consolidation.ipynb (análise completa)
```

**Tempo estimado para re-execução:** 5-10 minutos

### Pré-requisitos
- Python 3.8+ (Python 3.11 recomendado)
- ~500MB de espaço em disco
- Jupyter Notebook
- Dependências: pandas, numpy, matplotlib, seaborn, pyarrow

## 📈 Resultados Principais

Todos os resultados estão disponíveis em:
- **Visualizações**: `outputs/figures/` - 3 gráficos em PNG
- **Tabelas**: `outputs/tables/` - 3 arquivos CSV
- **Dados processados**: `gold/` - 3 arquivos Parquet analíticos

### Visualizações Geradas

**Medalhas por País (Top 50):**
1. `top50_medals_summer.png` - Top 50 países em Jogos de Verão
2. `top50_medals_winter.png` - Top 50 países em Jogos de Inverno  
3. `top50_medals_total.png` - Top 50 países no Total Geral

### Top 3 Países (Total Geral - 1896-2024)
1. 🥇 **Estados Unidos (USA)** - 3,009 medalhas
2. 🥈 **União Soviética (URS)** - 1,204 medalhas
3. 🥉 **Alemanha (GER)** - 1,098 medalhas

### Destaques Brasil e Cuba
- **Brasil (BRA)**: #31 global - 150 medalhas (🥇37 | 🥈42 | 🥉71)
- **Cuba (CUB)**: #24 global - 235 medalhas (🥇84 | 🥈69 | 🥉82)

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

## 🔍 Insights Principais

1. **Estados Unidos** domina o ranking geral com mais de 3,000 medalhas
2. **Europa e América** concentram a maioria das medalhas olímpicas
3. **Jogos de Verão** têm muito mais medalhas distribuídas que Jogos de Inverno
4. **Brasil** está na 31ª posição global, com destaque em esportes coletivos
5. **Cuba** está na 24ª posição global, com forte tradição em boxe e atletismo

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
