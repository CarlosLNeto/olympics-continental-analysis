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
BRONZE_PATH_PARTE1 = BASE_PATH / 'bronze' / 'parte1'
BRONZE_PATH_PARTE2 = BASE_PATH / 'bronze' / 'parte2'
METADATA_PATH_PARTE1 = BASE_PATH / 'metadata' / 'parte1'
METADATA_PATH_PARTE2 = BASE_PATH / 'metadata' / 'parte2'

# Criar diretórios de metadados se não existirem
METADATA_PATH_PARTE1.mkdir(parents=True, exist_ok=True)
METADATA_PATH_PARTE2.mkdir(parents=True, exist_ok=True)

def generate_metadata(parquet_file, description, source, file_path_prefix):
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
        "file_path": f"{file_path_prefix}/{parquet_file.name}",
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

# Datasets da pasta Gold (parte2)
gold_datasets_info = {
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

# Datasets da pasta Bronze
bronze_datasets_info = {
    "medals_integrated_1896_2024": {
        "description": "Dataset integrado de todas as medalhas olímpicas de 1896 a 2024, incluindo informações de atletas, países, modalidades e continentes",
        "source": "Integração dos dados brutos Olympics_1896_2022 e Olympics_Paris2024 com mapeamento de países para continentes"
    },
    "medals_integrated": {
        "description": "Dataset integrado de medalhas olímpicas processado para análises continentais",
        "source": "Processamento e limpeza de medals_integrated_1896_2024.parquet"
    }
}

def process_datasets(source_path, metadata_path, datasets_info, file_path_prefix, section_name):
    """Processa datasets de uma pasta específica"""
    
    print(f'\n📂 Processando {section_name}')
    print('='*60)
    
    # Listar todos os parquets
    parquet_files = sorted(source_path.glob('*.parquet'))
    print(f'\n📊 Total de arquivos Parquet em {section_name}: {len(parquet_files)}')
    
    if len(parquet_files) == 0:
        print(f'   Nenhum arquivo parquet encontrado em {source_path}')
        return 0, 0
    
    # Verificar quais já têm metadados
    existing_metadata = set(f.stem.replace('_metadata', '') for f in metadata_path.glob('*_metadata.json'))
    print(f'📄 Metadados existentes: {len(existing_metadata)}')
    
    # Gerar metadados para os que faltam
    missing_count = 0
    created_count = 0
    
    for parquet_file in parquet_files:
        dataset_name = parquet_file.stem
        metadata_file = metadata_path / f'{dataset_name}_metadata.json'
        
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
                    info['source'],
                    file_path_prefix
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
    
    return missing_count, created_count

print('='*80)
print('GERANDO METADADOS JSON PARA ARQUIVOS PARQUET')
print('='*80)

# Processar diferentes seções
total_missing = 0
total_created = 0
total_files = 0

# 1. Processar Gold/Parte2
missing, created = process_datasets(
    GOLD_PATH, 
    METADATA_PATH_PARTE2, 
    gold_datasets_info, 
    "gold/parte2",
    "GOLD/PARTE2"
)
total_missing += missing
total_created += created
total_files += len(list(GOLD_PATH.glob('*.parquet')))

# 2. Processar Bronze/Parte1
missing, created = process_datasets(
    BRONZE_PATH_PARTE1, 
    METADATA_PATH_PARTE1, 
    bronze_datasets_info, 
    "bronze/parte1",
    "BRONZE/PARTE1"
)
total_missing += missing
total_created += created
total_files += len(list(BRONZE_PATH_PARTE1.glob('*.parquet')))

# 3. Processar Bronze/Parte2
missing, created = process_datasets(
    BRONZE_PATH_PARTE2, 
    METADATA_PATH_PARTE2, 
    bronze_datasets_info, 
    "bronze/parte2",
    "BRONZE/PARTE2"
)
total_missing += missing
total_created += created
total_files += len(list(BRONZE_PATH_PARTE2.glob('*.parquet')))

print('\n' + '='*80)
print('RESUMO GERAL')
print('='*80)
print(f'Total de arquivos Parquet: {total_files}')
print(f'Metadados faltando: {total_missing}')
print(f'Metadados criados agora: {total_created}')

if total_created == total_missing:
    print('\n✅ TODOS OS METADADOS FORAM CRIADOS COM SUCESSO!')
else:
    print(f'\n⚠️  Ainda faltam {total_missing - total_created} metadados')

print('='*80)
