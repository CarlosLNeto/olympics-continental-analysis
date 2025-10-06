# 📁 Estrutura do Projeto - Data Lake

Este projeto segue uma arquitetura de **Data Lake** com organização em camadas e separação por partes/atividades.

## 🏗️ Arquitetura

```
AnalisesPorContinente/
│
├── raw/                    ← CAMADA RAW: Dados originais sem modificação
│   ├── parte1/             ← Dados brutos da Parte 1
│   │   ├── Olympics_1896_2022/
│   │   └── Olympics_Paris2024/
│   └── parte2/             ← Dados brutos da Parte 2 (a ser adicionado)
│
├── bronze/                 ← CAMADA BRONZE: Dados tratados e padronizados
│   ├── parte1/             ← Formato: Parquet
│   │   └── medals_integrated_1896_2024.parquet
│   └── parte2/             ← (a ser preenchido)
│
├── gold/                   ← CAMADA GOLD: Análises e resultados finais
│   ├── parte1/             ← Formato: Parquet
│   │   ├── medals_summer.parquet
│   │   ├── medals_winter.parquet
│   │   └── medals_total.parquet
│   └── parte2/             ← (a ser preenchido)
│
├── code/                   ← NOTEBOOKS: Análises em Jupyter
│   ├── parte1/
│   │   ├── parte1_analise_medalhas.ipynb
│   │   └── check_parquet.py
│   └── parte2/             ← (a ser adicionado)
│
├── metadata/               ← METADADOS: Descrições em JSON
│   ├── parte1/
│   │   ├── medals_summer_metadata.json
│   │   ├── medals_winter_metadata.json
│   │   └── medals_total_metadata.json
│   └── parte2/             ← (a ser adicionado)
│
└── outputs/                ← SAÍDAS: Para apresentação (não segue camadas)
    ├── figures/            ← Gráficos PNG (300 DPI)
    │   ├── top50_summer.png
    │   ├── top50_winter.png
    │   └── top50_total.png
    └── tables/             ← Tabelas HTML e CSV
        ├── medals_summer_full.html
        ├── medals_winter_full.html
        ├── medals_total_full.html
        ├── medals_summer.csv
        ├── medals_winter.csv
        └── medals_total.csv
```

## 📊 Camadas do Data Lake

### 1. **RAW** - Dados Brutos
- Dados originais sem nenhuma transformação
- Formatos variados (CSV, JSON, etc.)
- Imutável - nunca modificar

### 2. **BRONZE** - Dados Tratados
- Dados limpos e padronizados
- **Formato obrigatório: Parquet**
- Validações básicas aplicadas
- Tipos de dados corrigidos

### 3. **GOLD** - Dados Analíticos
- Resultados de análises e agregações
- **Formato obrigatório: Parquet**
- Dados prontos para consumo
- Otimizados para leitura

## 📝 Metadados

Cada arquivo Parquet nas camadas Bronze e Gold possui um arquivo JSON correspondente em `metadata/` contendo:

```json
{
  "nome": "Nome do dataset",
  "descricao": "Descrição detalhada",
  "periodo": "Período dos dados",
  "total_paises": 161,
  "total_medalhas": 45000,
  "colunas": ["rank", "country_noc", "gold", "silver", "bronze", "total"],
  "fonte": "Origem dos dados",
  "criado_em": "2024-10-05T..."
}
```

## 🔄 Fluxo de Dados

```
RAW (CSV, JSON)
    ↓ Limpeza, validação
BRONZE (Parquet)
    ↓ Agregações, análises
GOLD (Parquet)
    ↓ Exportação
OUTPUTS (HTML, PNG, CSV)
```

## 📚 Organização por Partes

- **Parte 1**: Análise de Medalhas Olímpicas por País (1896-2024)
- **Parte 2**: (A ser definido)

Cada parte tem sua própria estrutura completa de camadas, mantendo isolamento e organização.

## 🚀 Como Usar

### Executar Parte 1:
```bash
jupyter notebook code/parte1/parte1_analise_medalhas.ipynb
```

### Visualizar Resultados:
- **Tabelas HTML**: Abrir `outputs/tables/*.html` no navegador
- **Gráficos**: Abrir `outputs/figures/*.png`
- **Dados**: Ler arquivos Parquet em `gold/parte1/`

## 📦 Formato Parquet

Todos os dados nas camadas Bronze e Gold usam Parquet por:
- ✅ Compressão eficiente (menor espaço)
- ✅ Leitura rápida (colunar)
- ✅ Preserva tipos de dados
- ✅ Compatível com Pandas, Spark, DuckDB

## 🛠️ Dependências

Veja `requirements.txt` para lista completa de dependências Python necessárias.
