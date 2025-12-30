"""
Scan de filesystem em modo SOMENTE LEITURA.

Gera uma lista plana de arquivos a partir de um diretório raiz.
Caminhos e dados aqui são ilustrativos.
"""

from pathlib import Path

ROOT = Path("X:/exemplo_servidor")
OUTPUT = "lista_arquivos.txt"

def main():
    with open(OUTPUT, "w", encoding="utf-8") as f:
        for path in ROOT.rglob("*"):
            if path.is_file():
                f.write(str(path) + "\n")

if __name__ == "__main__":
    main()
