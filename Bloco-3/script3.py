import csv
from pathlib import Path

pasta_filiais = Path.cwd() / "planilhas_filiais"
pasta_filiais.mkdir(exist_ok=True)

(pasta_filiais / "filial_norte.csv").write_text(
    "Filial;Vendedor;Valor\nNorte;Ana;1500.00\nNorte;Carlos;2300.00\n", encoding="utf-8"
)
(pasta_filiais / "filial_sul.csv").write_text(
    "Filial;Vendedor;Valor\nSul;Mariana;3100.00\nSul;Pedro;950.00\n", encoding="utf-8"
)

arquivo_consolidado = pasta_filiais / "consolidado_geral.csv"
linhas_consolidadas = [["Filial", "Vendedor", "Valor"]]

for planilha in sorted(pasta_filiais.glob("filial_*.csv")):
    with planilha.open(mode="r", encoding="utf-8") as f:
        leitor = csv.reader(f, delimiter=";")
        next(leitor)  
        for linha in leitor:
            linhas_consolidadas.append(linha)

with arquivo_consolidado.open(mode="w", newline="", encoding="utf-8") as f:
    escritor = csv.writer(f, delimiter=";")
    escritor.writerows(linhas_consolidadas)

print(f"Consolidação concluída! Total de registros unidos: {len(linhas_consolidadas) - 1}")
