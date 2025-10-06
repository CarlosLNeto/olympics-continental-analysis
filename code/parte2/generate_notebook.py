#!/usr/bin/env python3
"""
Script para gerar notebook completo da Parte 2 com todas as implementações
"""

import json
from pathlib import Path

def create_complete_notebook():
    """Cria notebook completo da Parte 2"""
    
    notebook = {
        "cells": [],
        "metadata": {
            "kernelspec": {
                "display_name": "Python 3",
                "language": "python",
                "name": "python3"
            },
            "language_info": {
                "name": "python",
                "version": "3.11.0"
            }
        },
        "nbformat": 4,
        "nbformat_minor": 5
    }
    
    cells = []
    
    # Célula 0: Título
    cells.append({
        "cell_type": "markdown",
        "metadata": {},
        "source": [
            "# 📊 Parte 2 - Análise de Medalhas Olímpicas por Continente (1896-2024)\n",
            "\n",
            "## 🎯 Objetivos\n",
            "\n",
            "Análise completa da distribuição e evolução de medalhas olímpicas por **continente**:\n",
            "\n",
            "1. **2.1** - Distribuição total de medalhas por continente\n",
            "2. **2.2** - Crescimento da representação ao longo do tempo\n",
            "3. **2.3** - Participação feminina por continente\n",
            "4. **2.4** - Modalidades mais fortes por continente\n",
            "5. **2.5** - Crescimento nas medalhas entre 1896 e 2024\n",
            "\n",
            "---"
        ]
    })
    
    # Célula 1: Imports
    cells.append({
        "cell_type": "code",
        "execution_count": None,
        "metadata": {},
        "outputs": [],
        "source": [
            "import pandas as pd\n",
            "import numpy as np\n",
            "import matplotlib.pyplot as plt\n",
            "import seaborn as sns\n",
            "from pathlib import Path\n",
            "from datetime import datetime\n",
            "import json\n",
            "import warnings\n",
            "warnings.filterwarnings('ignore')\n",
            "\n",
            "# Configurações\n",
            "plt.style.use('seaborn-v0_8-whitegrid')\n",
            "sns.set_palette('Set2')\n",
            "plt.rcParams['figure.figsize'] = (14, 8)\n",
            "plt.rcParams['font.size'] = 11\n",
            "%matplotlib inline\n",
            "\n",
            "print('✅ Bibliotecas importadas!')"
        ]
    })
    
    # Célula 2: Paths
    cells.append({
        "cell_type": "code",
        "execution_count": None,
        "metadata": {},
        "outputs": [],
        "source": [
            "BASE_PATH = Path('../..')\n",
            "RAW_PATH = BASE_PATH / 'raw'\n",
            "BRONZE_PATH = BASE_PATH / 'bronze' / 'parte2'\n",
            "GOLD_PATH = BASE_PATH / 'gold' / 'parte2'\n",
            "METADATA_PATH = BASE_PATH / 'metadata' / 'parte2'\n",
            "OUTPUTS_PATH = BASE_PATH / 'outputs'\n",
            "\n",
            "# Criar diretórios\n",
            "for path in [BRONZE_PATH, GOLD_PATH, METADATA_PATH]:\n",
            "    path.mkdir(parents=True, exist_ok=True)\n",
            "(OUTPUTS_PATH / 'figures').mkdir(parents=True, exist_ok=True)\n",
            "(OUTPUTS_PATH / 'tables').mkdir(parents=True, exist_ok=True)\n",
            "\n",
            "print('✅ Caminhos configurados!')\n",
            "print(f'   RAW: {RAW_PATH} (compartilhado)')\n",
            "print(f'   BRONZE: {BRONZE_PATH}')\n",
            "print(f'   GOLD: {GOLD_PATH}')"
        ]
    })
    
    # Adicionar restante das células
    # (Continuarei nas próximas iterações devido ao tamanho)
    
    notebook["cells"] = cells
    return notebook

if __name__ == '__main__':
    nb = create_complete_notebook()
    output_path = Path('code/parte2/parte2_analise_continentes.ipynb')
    
    with open(output_path, 'w', encoding='utf-8') as f:
        json.dump(nb, f, indent=1, ensure_ascii=False)
    
    print(f"✅ Notebook criado: {output_path}")
