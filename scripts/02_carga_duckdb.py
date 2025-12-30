"""
Carga de lista de arquivos em DuckDB para análise exploratória.
"""

import duckdb

DB_PATH = "filesystem.duckdb"
TXT_INPUT = "lista_arquivos.txt"

con = duckdb.connect(DB_PATH)

con.execute("""
CREATE TABLE IF NOT EXISTS files (
    full_path TEXT
)
""")

con.execute("""
INSERT INTO files
SELECT * FROM read_csv_auto(?, delim='\n', header=False)
""", [TXT_INPUT])

con.close()
