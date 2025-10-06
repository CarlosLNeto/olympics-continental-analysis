# 🏅 Análises Olímpicas - Projeto Data Lake

[![Python](https://img.shields.io/badge/Python-3.8+-blue.svg)](https://www.python.org/)
[![Pandas](https://img.shields.io/badge/Pandas-1.5+-green.svg)](https://pandas.pydata.org/)
[![Parquet](https://img.shields.io/badge/Format-Parquet-red.svg)](https://parquet.apache.org/)
[![License](https://img.shields.io/badge/License-Educational-orange.svg)](LICENSE)

Projeto de análise de dados olímpicos implementando arquitetura de **Data Lake** com organização em camadas (Raw, Bronze, Gold) e separação por partes/atividades. Todos os dados processados são armazenados em formato **Parquet** para eficiência e compatibilidade.

## 🏗️ Arquitetura Data Lake

O projeto segue uma arquitetura de Data Lake moderna com:

```
📁 Estrutura:
  raw/          → Dados originais compartilhados (CSV, JSON)
  bronze/       → Dados tratados por parte (Parquet)
  gold/         → Análises finais por parte (Parquet)
  code/         → Notebooks Jupyter por parte
  metadata/     → Metadados JSON por parte
  outputs/      → Visualizações (HTML, PNG, CSV)

📊 Organização:
  • raw/ é compartilhado entre todas as partes
  • Cada parte tem seu próprio bronze/, gold/, code/, metadata/
  
  parte1/   → Análise de Medalhas por País (1896-2024) ✅
  parte2/   → (A ser adicionado)
```

### Características
- ✅ **Dados raw compartilhados**: Economia de espaço e consistência
- ✅ **Formato Parquet**: Todos os dados processados
- ✅ **Metadados JSON**: Documentação de cada dataset
- ✅ **Isolamento por parte**: Bronze, Gold, Code separados
- ✅ **Modular**: Fácil adicionar novas análises
- ✅ **Profissional**: Seguindo boas práticas de engenharia de dados

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

### 📊 Parte 1: Consolidação de Medalhas por País (1896-2024)

> **✨ Dados Completos:** Integração de dados históricos (1896-2022) + Paris 2024

**Três análises completas com rankings oficiais:**

1. **🌞 Medalhas - Jogos de Verão** (159 países)
   - Ranking consolidado de todas as edições incluindo Paris 2024
   - Gráfico Top 50 com distribuição Ouro/Prata/Bronze
   - Brasil e Cuba sempre visíveis com destaque

2. **❄️ Medalhas - Jogos de Inverno** (46 países)
   - Ranking consolidado de todas as edições de inverno
   - Análise focada em países com tradição em esportes de inverno

3. **🏆 Medalhas - Total Geral** (Verão + Inverno) (161 países)
   - Ranking combinado definitivo de 1896 a 2024
   - Top 50 países no pódio olímpico mundial

**Características:**
- ✅ Dados integrados de 1896 até Paris 2024 (128 anos de história)
- ✅ Rankings baseados nas fontes oficiais (Olympedia + Olympics.com)
- ✅ Visualizações profissionais com paleta de cores corporativa
- ✅ Tabelas HTML interativas e CSV para Excel
- ✅ Gráficos PNG em alta resolução (300 DPI)

### 📊 Parte 2: Análise de Medalhas por Continente (1896-2024)

> **✨ Análise Continental Completa:** Distribuição, crescimento e participação por continente

**Cinco análises completas com visualizações profissionais:**

1. **🌍 Distribuição Total por Continente**
   - Gráfico de pizza mostrando % de medalhas por continente
   - Europa lidera com maior concentração de medalhas
   - Separação entre Jogos de Verão e Inverno

2. **📈 Crescimento da Representação**
   - **Medalhistas**: Países que ganharam medalhas ao longo do tempo
   - **Participantes**: TODOS os países que participaram (novo!)
   - Análise comparativa revela democratização das Olimpíadas

3. **👩 Participação Feminina**
   - Evolução do percentual de medalhas conquistadas por mulheres
   - Análise por continente e por temporada (Verão/Inverno)
   - Crescimento significativo desde 1896

4. **🥋 Modalidades Fortes por Continente**
   - Top modalidades de cada continente
   - Identificação de especializações regionais

5. **📊 Crescimento em Medalhas (1896-2024)**
   - Análise de crescimento por período histórico
   - Comparação entre continentes

**Características:**
- ✅ Dados integrados: 316K+ resultados históricos + Paris 2024
- ✅ Dois tipos de gráficos: Medalhistas vs Participantes
- ✅ Insight importante: Brasil participa dos Jogos de Inverno desde 1992!
- ✅ Gráficos em alta resolução (300 DPI)
- ✅ Dados salvos em Parquet para análises futuras

**🔍 Descoberta Principal:**
- **Jogos de Inverno 2022 - Américas:**
  - 15 países PARTICIPARAM (incluindo Brasil 🇧🇷)
  - Apenas 2 países GANHARAM medalhas (EUA e Canadá)
  - Diferença revela democratização da participação vs concentração de medalhas

## 📂 Estrutura do Projeto

```
AnalisesPorContinente/
│
├── raw/                              # CAMADA RAW
│   └── Olympics_1896_2022/          # Dados históricos compartilhados
│       └── Olympics_Paris2024/       # Dados Paris 2024 compartilhados
│
├── bronze/                           # CAMADA BRONZE (Parquet)
│   ├── parte1/
│   │   └── medals_integrated_1896_2024.parquet
│   └── parte2/
│       └── medals_integrated.parquet
│
├── gold/                             # CAMADA GOLD (Parquet)
│   ├── parte1/
│   │   ├── medals_summer.parquet
│   │   ├── medals_winter.parquet
│   │   └── medals_total.parquet
│   └── parte2/
│       ├── medals_por_continente.parquet
│       ├── medals_evolucao_temporal_*.parquet
│       ├── participacao_*.parquet
│       └── crescimento_*.parquet
│
├── code/                             # NOTEBOOKS
│   ├── parte1/
│   │   ├── parte1_analise_medalhas.ipynb  # 🎯 Análise Medalhas
│   │   ├── check_parquet.py
│   │   └── README.md
│   └── parte2/
│       ├── parte2_analise_continentes.ipynb  # 🎯 Análise Continentes
│       └── noc_to_continent.py
│
├── metadata/                         # METADADOS (JSON)
│   ├── parte1/ ...
│   └── parte2/ ...
│
├── outputs/                          # OUTPUTS (não segue camadas)
│   ├── figures/                      # Gráficos PNG
│   │   ├── [Parte 1] top50_*.png
│   │   ├── [Parte 2] parte2_pizza_continente.png
│   │   ├── [Parte 2] parte2_evolucao_continente.png
│   │   ├── [Parte 2] parte2_crescimento_representacao.png
│   │   ├── [Parte 2] parte2_participacao_todos_paises.png  # NOVO!
│   │   └── [Parte 2] parte2_participacao_*.png
│   └── tables/                       # Tabelas HTML/CSV
│       └── medals_*.{html,csv}
│
├── 📄 README.md                      # Este arquivo
├── 📄 create_participation_graphs.py # Script reutilizável
├── 📄 requirements.txt               # Dependências
└── 📄 .gitignore
```

> **📖 Documentação detalhada**: Ver [ESTRUTURA.md](ESTRUTURA.md) para entender a arquitetura completa

## 🚀 Como Usar

### 📖 Opção 1: Visualizar Resultados (Recomendado)

Os resultados já estão prontos! Basta visualizar:

```bash
# Tabelas HTML interativas
open outputs/tables/medals_summer_full.html   # Mac
# ou
start outputs/tables/medals_summer_full.html  # Windows
# ou use seu navegador favorito

# Gráficos PNG
open outputs/figures/top50_summer.png

# Tabelas CSV
open outputs/tables/medals_summer.csv  # Excel/LibreOffice
```

### 🔄 Opção 2: Executar Análises

#### Parte 1: Análise de Medalhas por País
```bash
# 1. Instalar dependências
pip install -r requirements.txt

# 2. Abrir Jupyter
jupyter notebook

# 3. Navegar e abrir:
#    code/parte1/parte1_analise_medalhas.ipynb

# 4. Executar: Cell → Run All
```
**⏱️ Tempo estimado:** 2-5 minutos

#### Parte 2: Análise de Medalhas por Continente  
```bash
# 1. Abrir Jupyter (se ainda não estiver aberto)
jupyter notebook

# 2. Navegar e abrir:
#    code/parte2/parte2_analise_continentes.ipynb

# 3. IMPORTANTE: Verificar que o kernel é "Python 3.11"
#    (canto superior direito do notebook)

# 4. Executar: Kernel → Restart & Run All
```
**⏱️ Tempo estimado:** 3-7 minutos  
**⚠️ Nota:** Use sempre "Restart & Run All" para garantir execução correta

#### Script Independente: Gráficos de Participação
```bash
# Gerar gráficos de participação (todos os países)
python3.11 create_participation_graphs.py
```
**⏱️ Tempo estimado:** 1-2 minutos

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

### 🌍 Distribuição por Continente (Total Geral)

| Continente | % Medalhas | Características |
|------------|-----------|-----------------|
| 🇪🇺 **Europa** | ~55% | Domínio histórico, tradição esportiva |
| 🌎 **Américas** | ~25% | Lideradas por EUA, crescimento sul-americano |
| 🌏 **Ásia** | ~15% | Crescimento acelerado, China e Japão fortes |
| 🌍 **África** | ~3% | Concentração em atletismo e futebol |
| 🌊 **Oceania** | ~2% | Austrália domina a região |

### 🌎 Destaque: Brasil e Cuba

| País | Ranking | 🥇 Ouro | 🥈 Prata | 🥉 Bronze | Total |
|------|---------|----------|-----------|-----------|--------|
| 🇧🇷 **Brasil** | **30º** | 40 | 49 | 81 | **170** |
| 🇨🇺 **Cuba** | **23º** | 86 | 70 | 88 | **244** |

> 💡 **Incluindo Paris 2024:** Brasil conquistou 20 medalhas (3🥇 7🥈 10🥉) em Paris 2024!

### ❄️ Brasil nos Jogos de Inverno

- **Participa desde:** 1992 (Albertville)
- **Medalhas conquistadas:** 0
- **Insight importante:** Brasil está entre os 15 países das Américas que participam dos Jogos de Inverno, mas ainda não conquistou medalhas
- **Diferença:** Participação ≠ Medalhas (democratização vs desempenho competitivo)

### 📊 Visualizações Disponíveis

**Parte 1 - Análise por País:**

🖼️ **Gráficos (PNG - Alta Resolução):**
- `outputs/figures/top50_summer.png` - Top 50 países em Jogos de Verão
- `outputs/figures/top50_winter.png` - Top 50 países em Jogos de Inverno
- `outputs/figures/top50_total.png` - Top 50 países no Total Geral

📋 **Tabelas (CSV - Prontas para Excel):**
- `outputs/tables/medals_summer.csv` - Ranking completo Jogos de Verão
- `outputs/tables/medals_winter.csv` - Ranking completo Jogos de Inverno
- `outputs/tables/medals_total.csv` - Ranking completo Total Geral

**Parte 2 - Análise por Continente:**

🖼️ **Gráficos (PNG - Alta Resolução):**
- `outputs/figures/parte2_pizza_continente.png` - Distribuição por continente
- `outputs/figures/parte2_evolucao_continente.png` - Evolução temporal
- `outputs/figures/parte2_crescimento_representacao.png` - Países medalhistas
- `outputs/figures/parte2_participacao_todos_paises.png` - **TODOS** os países participantes
- `outputs/figures/parte2_participacao_feminina.png` - Participação feminina
- `outputs/figures/parte2_participacao_atletas_femininas.png` - Atletas femininas

📊 **Comparação Importante:**
- **parte2_crescimento_representacao.png**: Apenas países que GANHARAM medalhas
- **parte2_participacao_todos_paises.png**: TODOS os países participantes
- **Diferença**: Revela democratização da participação vs concentração de medalhas

💾 **Dados Processados (Parquet - Para análises):**
- `gold/parte1/medals_*.parquet` + metadados
- `gold/parte2/medals_*.parquet` + metadados
- `gold/parte2/participacao_*.parquet` + metadados

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
