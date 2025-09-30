# 🏅 Análise de Dados Olímpicos por Continente

[![Python](https://img.shields.io/badge/Python-3.8+-blue.svg)](https://www.python.org/)
[![Pandas](https://img.shields.io/badge/Pandas-1.5+-green.svg)](https://pandas.pydata.org/)
[![License](https://img.shields.io/badge/License-Educational-orange.svg)](LICENSE)

Este repositório contém análises completas de dados das Olimpíadas (1896-2024), focando em comparações entre continentes, países e evolução histórica. O projeto implementa uma arquitetura de **Data Lake** com camadas Bronze e Gold, utilizando formato **Parquet** para armazenamento eficiente.

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

### Parte 1: Consolidação de Medalhas por País
- ✅ Total de medalhas por país (Verão, Inverno e Total Geral)
- ✅ Rankings oficiais compatíveis com Wikipedia
- ✅ Visualizações dos Top 50 países
- ✅ Gráficos de barras horizontais empilhadas (Ouro/Prata/Bronze)

### Parte 2: Análise por Continente
- ✅ **2.1** Distribuição total de medalhas por continente
  - Total acumulado e por edição
  - Gráficos: pizza e linha temporal
  - Estatísticas de atletas por continente
  
- ✅ **2.2** Crescimento da representação ao longo do tempo
  - Média, desvio padrão e mediana
  - Gráficos de evolução temporal
  - Taxa de crescimento por década
  
- ✅ **2.3** Participação feminina por continente
  - Percentual de mulheres por edição
  - Evolução histórica
  - Comparação entre continentes
  
- ✅ **2.4** Modalidades mais fortes por continente
  - Top 5 esportes com mais medalhas
  - Análise de especialização regional
  
- ✅ **2.5** Crescimento nas medalhas entre 1986 e 2024
  - Comparação de períodos
  - Crescimento absoluto e percentual
  - Identificação de continentes emergentes

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
├── bronze/                           # Camada Bronze - Dados limpos
│   ├── *.parquet                     # Dados em formato Parquet
│   ├── *_metadata.json               # Metadados de cada arquivo
│   ├── noc_continent_mapping.parquet # Mapeamento país→continente
│   ├── medals_by_continent.parquet   # Medalhas + continente
│   └── athletes_by_continent.parquet # Atletas + continente + sexo
│
├── gold/                             # Camada Gold - Dados analíticos
│   ├── medals_summer_consolidated.parquet
│   ├── medals_winter_consolidated.parquet
│   ├── medals_total_consolidated.parquet
│   ├── medals_by_continent_total.parquet
│   ├── medals_by_year_continent.parquet
│   ├── avg_athletes_by_continent.parquet
│   ├── representation_stats_by_continent.parquet
│   ├── female_participation_by_continent.parquet
│   ├── top_sports_by_continent.parquet
│   ├── medals_growth_1986_2024.parquet
│   └── *_metadata.json               # Metadados de cada análise
│
├── notebooks/                        # Jupyter Notebooks
│   ├── 01_bronze_layer_processing.ipynb
│   ├── 02_part1_medals_consolidation.ipynb
│   ├── 03a_part2_continent_analysis_q1.ipynb
│   └── 03b_part2_continent_analysis_q2-5.ipynb
│
├── outputs/                          # Saídas para apresentação
│   ├── tables/                       # Tabelas em CSV
│   │   ├── medals_summer_consolidated.csv
│   │   ├── medals_winter_consolidated.csv
│   │   ├── medals_total_consolidated.csv
│   │   ├── medals_by_continent_total.csv
│   │   └── ...
│   └── figures/                      # Gráficos em PNG
│       ├── top50_medals_summer.png
│       ├── top50_medals_winter.png
│       ├── top50_medals_total.png
│       ├── medals_by_continent_pie.png
│       ├── medals_by_year_continent_line.png
│       ├── athletes_growth_by_continent.png
│       ├── female_participation_evolution.png
│       ├── top_sports_by_continent.png
│       └── medals_growth_comparison.png
│
├── requirements.txt                  # Dependências Python
├── .gitignore                        # Arquivos ignorados pelo Git
└── README.md                         # Este arquivo
```

## 🚀 Como Usar

### 1. Clonar o Repositório
```bash
git clone https://github.com/CarlosLNeto/olympics-continental-analysis.git
cd olympics-continental-analysis
```

### 2. Instalar Dependências
```bash
# Criar ambiente virtual (recomendado)
python -m venv venv
source venv/bin/activate  # No Windows: venv\Scripts\activate

# Instalar dependências
pip install -r requirements.txt
```

### 3. Executar Notebooks
```bash
jupyter notebook
```

Executar os notebooks na ordem:
1. `01_bronze_layer_processing.ipynb` - Processa dados raw → bronze
2. `02_part1_medals_consolidation.ipynb` - Análise Parte 1
3. `03a_part2_continent_analysis_q1.ipynb` - Análise Parte 2 (Q1)
4. `03b_part2_continent_analysis_q2-5.ipynb` - Análise Parte 2 (Q2-5)

## 📈 Resultados Principais

### Top 3 Países (Total Geral)
1. 🥇 **Estados Unidos (USA)** - Maior potência olímpica histórica
2. 🥈 **União Soviética/Rússia** - Forte em Inverno e Verão
3. 🥉 **Grã-Bretanha (GBR)** - Tradição histórica

### Distribuição por Continente
- **Europa**: ~45% das medalhas históricas
- **América**: ~30% (dominada por USA)
- **Ásia**: ~15% (crescimento acelerado)
- **Oceania**: ~5% (Australia e Nova Zelândia)
- **África**: ~5% (crescimento recente)

### Participação Feminina
- **1896**: 0% (proibida)
- **2022**: ~48% (quase paridade)
- Crescimento exponencial após 1980

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

1. **Europa domina historicamente**, mas Ásia está crescendo rapidamente
2. **Participação feminina** cresceu de 0% para quase 50% em 126 anos
3. **EUA lidera** em total geral, mas Noruega domina Jogos de Inverno per capita
4. **África e Ásia** mostram maior crescimento percentual desde 1986
5. **Atletismo** é a modalidade com mais medalhas distribuídas globalmente

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
