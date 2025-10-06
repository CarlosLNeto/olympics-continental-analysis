#!/usr/bin/env python3
"""
Script para verificar se o código do notebook está correto.
Execute este script para testar se df_medals terá athlete_id quando reiniciar o notebook.
"""

import json

def check_notebook():
    print("="*80)
    print("VERIFICAÇÃO DO NOTEBOOK - athlete_id")
    print("="*80)
    
    with open('code/parte2/parte2_analise_continentes.ipynb', 'r') as f:
        nb = json.load(f)
    
    issues = []
    checks = []
    
    # Check 1: cols definition
    print("\n✓ Check 1: Verificando definição de 'cols'...")
    found_cols = False
    for i, cell in enumerate(nb['cells']):
        if cell['cell_type'] == 'code':
            source = ''.join(cell['source'])
            if "cols=[" in source and "'athlete_id'" in source:
                print(f"  ✅ Célula {i}: cols inclui 'athlete_id'")
                found_cols = True
                # Extract the line
                for line in source.split('\n'):
                    if 'cols=[' in line:
                        print(f"     {line.strip()}")
                checks.append("cols has athlete_id")
                break
    
    if not found_cols:
        print("  ❌ PROBLEMA: cols NÃO tem 'athlete_id'")
        issues.append("cols missing athlete_id")
    
    # Check 2: df_p athlete_id creation
    print("\n✓ Check 2: Verificando criação de athlete_id em df_p (Paris 2024)...")
    found_df_p = False
    for i, cell in enumerate(nb['cells']):
        if cell['cell_type'] == 'code':
            source = ''.join(cell['source'])
            if "df_p['athlete_id']" in source or 'df_p["athlete_id"]' in source:
                print(f"  ✅ Célula {i}: df_p['athlete_id'] é criado")
                for line in source.split('\n'):
                    if 'athlete_id' in line and 'df_p' in line:
                        print(f"     {line.strip()}")
                found_df_p = True
                checks.append("df_p has athlete_id creation")
                break
    
    if not found_df_p:
        print("  ❌ PROBLEMA: df_p['athlete_id'] NÃO é criado")
        issues.append("df_p missing athlete_id creation")
    
    # Check 3: df_h merge with athletes
    print("\n✓ Check 3: Verificando merge de df_h com df_hist_athletes...")
    found_merge = False
    for i, cell in enumerate(nb['cells']):
        if cell['cell_type'] == 'code':
            source = ''.join(cell['source'])
            if "df_h.merge" in source and "df_hist_athletes" in source and "athlete_id" in source:
                print(f"  ✅ Célula {i}: df_h faz merge com df_hist_athletes")
                for line in source.split('\n'):
                    if 'df_h.merge' in line and 'athletes' in line:
                        print(f"     {line.strip()}")
                found_merge = True
                checks.append("df_h merges with athletes")
                break
    
    if not found_merge:
        print("  ❌ PROBLEMA: df_h NÃO faz merge com df_hist_athletes")
        issues.append("df_h missing athlete merge")
    
    # Check 4: df_medals creation with cols
    print("\n✓ Check 4: Verificando criação de df_medals com cols...")
    found_concat = False
    for i, cell in enumerate(nb['cells']):
        if cell['cell_type'] == 'code':
            source = ''.join(cell['source'])
            if "df_medals=pd.concat" in source and "[df_h[cols],df_p[cols]]" in source:
                print(f"  ✅ Célula {i}: df_medals usa concat com cols")
                for line in source.split('\n'):
                    if 'df_medals=' in line and 'concat' in line:
                        print(f"     {line.strip()}")
                found_concat = True
                checks.append("df_medals uses cols in concat")
                break
    
    if not found_concat:
        print("  ❌ PROBLEMA: df_medals NÃO usa concat com cols corretamente")
        issues.append("df_medals concat issue")
    
    # Summary
    print("\n" + "="*80)
    print("RESUMO DA VERIFICAÇÃO")
    print("="*80)
    
    if not issues:
        print("\n✅ ✅ ✅ TUDO CORRETO! ✅ ✅ ✅")
        print("\nO código está perfeito. Quando você reiniciar o notebook:")
        print("  • df_h terá athlete_id (do merge com df_hist_athletes)")
        print("  • df_p terá athlete_id (criado de code_athlete)")
        print("  • df_medals terá athlete_id (combinação de ambos)")
        print("  • Seção 2.3.1 funcionará sem erros")
        print("\n⚠️  IMPORTANTE: VOCÊ DEVE REINICIAR O KERNEL!")
        print("    Jupyter: Kernel → Restart & Run All")
        print("    Isso é ESSENCIAL porque df_medals precisa ser recriado.")
        print("\n    Se você só executar células individuais, df_medals antigo")
        print("    (sem athlete_id) ainda estará na memória!")
    else:
        print(f"\n❌ ENCONTRADOS {len(issues)} PROBLEMAS:")
        for issue in issues:
            print(f"  • {issue}")
        print("\nO código precisa ser corrigido antes de funcionar.")
    
    print("\n" + "="*80)
    
    return len(issues) == 0

if __name__ == '__main__':
    success = check_notebook()
    exit(0 if success else 1)
