"""
Filtro final de scripts autorais relevantes.
"""

import pandas as pd

INPUT = "scripts_python_encontrados.csv"
OUTPUT = "scripts_relevantes.csv"

df = pd.read_csv(INPUT)

exclusoes = [
    "site-packages",
    "__pycache__",
    "venv",
    "Lib\\",
    "Scripts\\"
]

mask = ~df["full_path"].str.contains("|".join(exclusoes), case=False, na=False)
df_filtrado = df[mask]

df_filtrado.to_csv(OUTPUT, index=False)

print(f"Scripts relevantes: {len(df_filtrado)}")
