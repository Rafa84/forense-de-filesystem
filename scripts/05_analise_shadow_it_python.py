"""
Identificação de arquivos Python e redução de ruído
(libs, venvs, backups históricos).
"""

import duckdb
import re

con = duckdb.connect("filesystem.duckdb")

query = """
SELECT full_path
FROM files
WHERE full_path LIKE '%.py'
"""

paths = [row[0] for row in con.execute(query).fetchall()]

def eh_ruido(path: str) -> bool:
    padroes = [
        "site-packages",
        "__pycache__",
        "venv",
        "Lib\\",
        "Scripts\\"
    ]
    return any(p.lower() in path.lower() for p in padroes)

scripts_relevantes = [p for p in paths if not eh_ruido(p)]

print(f"Scripts Python encontrados: {len(paths)}")
print(f"Scripts relevantes após filtro: {len(scripts_relevantes)}")

con.close()
