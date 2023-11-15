import sys
import os

# Adiciona o diretório raiz do projeto ao sys.path
projeto_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
if projeto_dir not in sys.path:
    sys.path.append(projeto_dir)
