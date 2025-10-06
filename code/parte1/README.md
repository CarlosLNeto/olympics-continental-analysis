# 📊 Parte 1 - Análise de Medalhas Olímpicas

## 🎯 Objetivo

Análise consolidada de medalhas olímpicas por país, integrando dados históricos (1896-2022) com dados recentes de Paris 2024.

## 📁 Arquivos

### Notebooks
- **`parte1_analise_medalhas.ipynb`** - Notebook principal com todas as análises
- **`check_parquet.py`** - Utilitário para validar arquivos Parquet

## 🔄 Pipeline de Dados

### 1. Raw → Bronze
- Integração de Olympics 1896-2022 + Paris 2024
- Tratamento de duplicatas
- Consolidação de eventos especiais (1956 Equestrian)
- Saída: `bronze/parte1/medals_integrated_1896_2024.parquet`

### 2. Bronze → Gold
- Agregação por país e temporada (Verão/Inverno)
- Cálculo de rankings
- Saídas:
  - `gold/parte1/medals_summer.parquet`
  - `gold/parte1/medals_winter.parquet`
  - `gold/parte1/medals_total.parquet`

### 3. Gold → Outputs
- Tabelas HTML profissionais
- Gráficos verticais Top 50
- Exportação CSV

## 📊 Análises Realizadas

1. **Medalhas - Jogos de Verão** (159 países)
2. **Medalhas - Jogos de Inverno** (46 países)
3. **Medalhas - Total Geral** (161 países)

## 🎨 Visualizações

### Tabelas HTML
- Design profissional minimalista
- Paleta azul corporativa
- Destaque para Top 3 e Brasil/Cuba
- Responsivo e pronto para impressão

### Gráficos PNG
- Barras verticais empilhadas
- Top 50 países
- 300 DPI para alta qualidade
- Cores profissionais (ouro/prata/bronze)

## 🚀 Como Executar

```bash
# 1. Navegar até o diretório do projeto
cd /caminho/para/AnalisesPorContinente

# 2. Ativar ambiente virtual (se houver)
source venv/bin/activate  # Linux/Mac
# ou
venv\Scripts\activate  # Windows

# 3. Executar notebook
jupyter notebook code/parte1/parte1_analise_medalhas.ipynb

# 4. No Jupyter: Cell → Run All
```

## 📈 Resultados Principais

### Top 3 - Total Geral (1896-2024)
1. 🥇 **Estados Unidos (USA)** - 3,135 medalhas
2. 🥈 **União Soviética (URS)** - 1,204 medalhas
3. 🥉 **Alemanha (GER)** - 1,131 medalhas

### Destaques
- 🇧🇷 **Brasil (BRA)**: 30º lugar - 170 medalhas (40🥇 49🥈 81🥉)
- 🇨🇺 **Cuba (CUB)**: 23º lugar - 244 medalhas (86🥇 70🥈 88🥉)

### Curiosidade
- 🇱🇮 **Liechtenstein (LIE)**: Único país que compete APENAS em Jogos de Inverno (29º lugar, 10 medalhas)

## 📂 Outputs Gerados

### Camada Gold (Parquet)
- `medals_summer.parquet` - 159 países
- `medals_winter.parquet` - 46 países
- `medals_total.parquet` - 161 países

### Visualizações
- `outputs/figures/top50_summer.png`
- `outputs/figures/top50_winter.png`
- `outputs/figures/top50_total.png`

### Tabelas
- `outputs/tables/medals_*_full.html` - Tabelas interativas completas
- `outputs/tables/medals_*.csv` - Para Excel

## 🔍 Metadados

Cada arquivo Parquet tem metadados correspondentes em `metadata/parte1/`:
- `medals_summer_metadata.json`
- `medals_winter_metadata.json`
- `medals_total_metadata.json`

## 📚 Fontes de Dados

- **Olympedia.org** - Dados históricos 1896-2022
- **Olympics.com** - Paris 2024
- **Kaggle** - Dataset Paris 2024

## ⏱️ Tempo de Execução

- **Total**: ~2-5 minutos
- **Integração (Raw → Bronze)**: ~30s
- **Análises (Bronze → Gold)**: ~1min
- **Visualizações**: ~1-3min

## 🛠️ Dependências

Principais bibliotecas necessárias:
- pandas >= 1.5.0
- numpy >= 1.23.0
- matplotlib >= 3.6.0
- seaborn >= 0.12.0
- pyarrow >= 10.0.0

Ver `requirements.txt` na raiz do projeto para lista completa.
