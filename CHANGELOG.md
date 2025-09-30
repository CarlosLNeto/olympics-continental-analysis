# 📝 Changelog

## [1.1.0] - 2024-09-30

### ✨ Adicionado
- **Novo notebook consolidado**: `00_resultados_completos.ipynb`
  - Apresenta todos os resultados em formato limpo e organizado
  - Ideal para apresentações e revisão rápida
  - Inclui visualizações lado a lado para comparação
  - Resumo executivo completo ao final

### 🔧 Corrigido
- **Notebook corrompido**: Recriado `03a_part2_continent_analysis_q1.ipynb`
  - Problema de corrupção resolvido
  - Funcionalidade totalmente restaurada
  - Questão 2.1 operacional

- **Fontes de dados**: URLs corrigidas nos metadados
  - Dados históricos: Base dos Dados (https://basedosdados.org/dataset/62f8cb83-ac37-48be-874b-b94dd92d3e2b)
  - Dados Paris 2024: Kaggle (https://www.kaggle.com/datasets/piterfm/paris-2024-olympic-summer-games/data)

### 📝 Atualizado
- **Autoria**: Todos os documentos e notebooks atualizados com:
  - Carlos Lavor Neto - Engenharia de Computação - UEA
  - Alexandro Pantoja - Orientador - UEA

- **Metadados JSON**: 
  - `raw/Olympics_1896_2022/metadata.json` - URL e fonte atualizadas
  - `raw/Olympics_Paris2024/metadata.json` - URL e fonte atualizadas

- **Documentação**:
  - `README.md` - Autores e fontes corrigidas
  - `PROJETO_RESUMO.md` - Autores atualizados

- **Notebooks**:
  - `02_part1_medals_consolidation.ipynb` - Autores adicionados
  - `03a_part2_continent_analysis_q1.ipynb` - Recriado com autores
  - `03b_part2_continent_analysis_q2-5.ipynb` - Autores adicionados

---

## [1.0.0] - 2024-09-30

### ✨ Release Inicial
- Estrutura completa Data Lake (raw → bronze → gold)
- 4 Jupyter Notebooks de análise
- Parte 1: Consolidação de medalhas por país
- Parte 2: Análise completa por continente (5 perguntas)
- 12+ visualizações profissionais
- 10+ tabelas consolidadas
- Mapeamento NOC → Continente (230+ países)
- Metadados JSON para todos os datasets
- Documentação completa

### 🎯 Funcionalidades
#### Parte 1
- Top 50 países - Jogos de Verão
- Top 50 países - Jogos de Inverno
- Top 50 países - Total Geral
- Gráficos de barras horizontais empilhadas

#### Parte 2
- Q2.1: Distribuição de medalhas por continente
- Q2.2: Crescimento da representação
- Q2.3: Participação feminina
- Q2.4: Modalidades mais fortes
- Q2.5: Crescimento 1986-2024

### 📊 Datasets
- Olympics 1896-2022: 135K+ atletas, 270K+ resultados
- Olympics Paris 2024: 11K+ atletas, 329 eventos

### 🛠️ Tecnologias
- Python 3.8+
- Pandas, NumPy
- Matplotlib, Seaborn
- PyArrow (Parquet)
- Jupyter Notebooks

---

## Estrutura de Versionamento

Seguimos Semantic Versioning (SemVer):
- **MAJOR**: Mudanças incompatíveis na API
- **MINOR**: Novas funcionalidades compatíveis
- **PATCH**: Correções de bugs

---

## Links

- **Repositório**: https://github.com/CarlosLNeto/olympics-continental-analysis
- **Documentação**: [README.md](README.md)
- **Instruções**: [INSTRUCOES.md](INSTRUCOES.md)
- **Resumo**: [PROJETO_RESUMO.md](PROJETO_RESUMO.md)
