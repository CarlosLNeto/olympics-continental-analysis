#!/usr/bin/env python3
"""
Script para gerar metadados JSON para todos os arquivos Parquet que não têm metadados
"""

import pandas as pd
import json
from pathlib import Path
from datetime import datetime

# Paths
BASE_PATH = Path.cwd()
GOLD_PATH = BASE_PATH / 'gold' / 'parte2'
METADATA_PATH = BASE_PATH / 'metadata' / 'parte2'

# Criar diretório de metadados se não existir
METADATA_PATH.mkdir(parents=True, exist_ok=True)

def generate_metadata(parquet_file, description, source):
    """Gera metadados para um arquivo parquet"""
    
    # Carregar parquet
    df = pd.read_parquet(parquet_file)
    
    # Nome do arquivo sem extensão
    dataset_name = parquet_file.stem
    
    # Coletar informações
    metadata = {
        "dataset_name": dataset_name,
        "description": description,
        "source": source,
        "creation_date": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
        "file_path": f"gold/parte2/{parquet_file.name}",
        "format": "parquet",
        "dimensions": {
            "rows": len(df),
            "columns": len(df.columns)
        },
        "columns": list(df.columns),
        "dtypes": {col: str(dtype) for col, dtype in df.dtypes.items()},
        "missing_values": df.isnull().sum().to_dict(),
        "memory_usage_mb": df.memory_usage(deep=True).sum() / (1024**2),
        "index_name": df.index.name if df.index.name else None,
        "sample_values": df.head(3).to_dict() if len(df) > 0 else {}
    }
    
    return metadata

# Definir descrições para cada dataset
datasets_info = {
    "crescimento_stats_summer": {
        "description": "Estatísticas de crescimento de países participantes (medalhistas) nos Jogos de Verão por continente",
        "source": "Calculado a partir de medals_integrated.parquet - agregação temporal de países que ganharam medalhas"
    },
    "crescimento_stats_winter": {
        "description": "Estatísticas de crescimento de países participantes (medalhistas) nos Jogos de Inverno por continente",
        "source": "Calculado a partir de medals_integrated.parquet - agregação temporal de países que ganharam medalhas"
    },
    "crescimento_temporal_summer": {
        "description": "Evolução temporal do número de países medalhistas nos Jogos de Verão por continente e ano",
        "source": "Calculado a partir de medals_integrated.parquet - contagem de países únicos por ano que ganharam medalhas"
    },
    "crescimento_temporal_winter": {
        "description": "Evolução temporal do número de países medalhistas nos Jogos de Inverno por continente e ano",
        "source": "Calculado a partir de medals_integrated.parquet - contagem de países únicos por ano que ganharam medalhas"
    },
    "crescimento_temporal": {
        "description": "Evolução temporal do número de países medalhistas combinando Verão e Inverno (legado)",
        "source": "Calculado a partir de medals_integrated.parquet - versão combinada (mantido para compatibilidade)"
    },
    "medals_evolucao_temporal": {
        "description": "Evolução temporal do número de medalhas por continente e ano (Verão e Inverno combinados)",
        "source": "Agregação de medals_integrated.parquet por ano e continente"
    },
    "medals_evolucao_temporal_summer": {
        "description": "Evolução temporal do número de medalhas por continente nos Jogos de Verão",
        "source": "Agregação de medals_integrated.parquet filtrado para game_season='Summer'"
    },
    "medals_evolucao_temporal_winter": {
        "description": "Evolução temporal do número de medalhas por continente nos Jogos de Inverno",
        "source": "Agregação de medals_integrated.parquet filtrado para game_season='Winter'"
    },
    "participacao_feminina_summer": {
        "description": "Percentual de medalhas conquistadas por mulheres nos Jogos de Verão por continente e ano",
        "source": "Calculado a partir de medals_integrated.parquet - proporção de medalhas femininas"
    },
    "participacao_feminina_winter": {
        "description": "Percentual de medalhas conquistadas por mulheres nos Jogos de Inverno por continente e ano",
        "source": "Calculado a partir de medals_integrated.parquet - proporção de medalhas femininas"
    },
    "participacao_atletas_femininas_summer": {
        "description": "Percentual de ATLETAS femininas participantes nos Jogos de Verão (contagem única por atleta)",
        "source": "Calculado a partir de medals_integrated.parquet usando athlete_id para contagem única"
    },
    "participacao_atletas_femininas_winter": {
        "description": "Percentual de ATLETAS femininas participantes nos Jogos de Inverno (contagem única por atleta)",
        "source": "Calculado a partir de medals_integrated.parquet usando athlete_id para contagem única"
    },
    "participacao_todos_paises_summer": {
        "description": "Número de TODOS os países participantes dos Jogos de Verão por continente e ano (não apenas medalhistas)",
        "source": "Calculado a partir de world_olympedia_olympics_athlete_event_result.csv + Paris 2024 athletes.csv"
    },
    "participacao_todos_paises_winter": {
        "description": "Número de TODOS os países participantes dos Jogos de Inverno por continente e ano (não apenas medalhistas)",
        "source": "Calculado a partir de world_olympedia_olympics_athlete_event_result.csv"
    },
    "participacao_todos_paises_stats_summer": {
        "description": "Estatísticas de participação de TODOS os países nos Jogos de Verão (média, desvio, min, max)",
        "source": "Estatísticas calculadas a partir de participacao_todos_paises_summer.parquet"
    },
    "participacao_todos_paises_stats_winter": {
        "description": "Estatísticas de participação de TODOS os países nos Jogos de Inverno (média, desvio, min, max)",
        "source": "Estatísticas calculadas a partir de participacao_todos_paises_winter.parquet"
    },
}

print('='*80)
print('GERANDO METADADOS JSON PARA ARQUIVOS PARQUET')
print('='*80)

# Listar todos os parquets
parquet_files = sorted(GOLD_PATH.glob('*.parquet'))
print(f'\n📊 Total de arquivos Parquet: {len(parquet_files)}')

# Verificar quais já têm metadados
existing_metadata = set(f.stem.replace('_metadata', '') for f in METADATA_PATH.glob('*_metadata.json'))
print(f'📄 Metadados existentes: {len(existing_metadata)}')

# Gerar metadados para os que faltam
missing_count = 0
created_count = 0

for parquet_file in parquet_files:
    dataset_name = parquet_file.stem
    metadata_file = METADATA_PATH / f'{dataset_name}_metadata.json'
    
    if dataset_name in existing_metadata:
        print(f'✓ {dataset_name} - metadados já existem')
        continue
    
    missing_count += 1
    
    # Obter informações do dataset
    if dataset_name in datasets_info:
        info = datasets_info[dataset_name]
        print(f'\n📝 Gerando: {dataset_name}_metadata.json')
        
        try:
            metadata = generate_metadata(
                parquet_file,
                info['description'],
                info['source']
            )
            
            # Salvar JSON
            with open(metadata_file, 'w', encoding='utf-8') as f:
                json.dump(metadata, f, indent=2, ensure_ascii=False)
            
            print(f'   ✅ Criado com sucesso!')
            print(f'   Dimensões: {metadata["dimensions"]["rows"]} linhas x {metadata["dimensions"]["columns"]} colunas')
            created_count += 1
            
        except Exception as e:
            print(f'   ❌ Erro: {e}')
    else:
        print(f'⚠️  {dataset_name} - sem descrição definida (pulando)')

print('\n' + '='*80)
print('RESUMO')
print('='*80)
print(f'Total de arquivos Parquet: {len(parquet_files)}')
print(f'Metadados existentes: {len(existing_metadata)}')
print(f'Metadados faltando: {missing_count}')
print(f'Metadados criados agora: {created_count}')
print(f'Total de metadados agora: {len(existing_metadata) + created_count}')

if created_count == missing_count:
    print('\n✅ TODOS OS METADADOS FORAM CRIADOS COM SUCESSO!')
else:
    print(f'\n⚠️  Ainda faltam {missing_count - created_count} metadados')

print('='*80)
