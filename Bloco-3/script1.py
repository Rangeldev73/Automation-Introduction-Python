import csv
from pathlib import Path

pasta_planilhas = Path.cwd() / "planilhas_geradas"
pasta_planilhas.mkdir(exist_ok=True)

arquivo_csv = pasta_planilhas / "vendas.csv"

dados_vendas = [
    ["Produto", "Quantidade", "Preco_Unitario"],
    ["Teclado Mecânico", 5, 250.00],
    ["Mouse Sem Fio", 12, 85.50],
    ["Monitor 24 Polegadas", 3, 890.00],
    ["Headset USB", 8, 140.00],
]

with arquivo_csv.open(mode="w", newline="", encoding="utf-8") as arquivo:
    escritor = csv.writer(arquivo, delimiter=";") 
    escritor.writerows(dados_vendas)

print(f"Planilha criada com sucesso em: {arquivo_csv}")
