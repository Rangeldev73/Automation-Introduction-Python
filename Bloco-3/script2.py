import csv
from pathlib import Path

pasta_planilhas = Path.cwd() / "planilhas_geradas"
arquivo_entrada = pasta_planilhas / "vendas.csv"
arquivo_saida = pasta_planilhas / "relatorio_destaques.csv"

if not arquivo_entrada.exists():
    print("Erro: Rode o script1.py primeiro para gerar a planilha base!")
else:
    destaques = [["Produto", "Quantidade", "Preco_Unitario", "Faturamento_Total"]]

    with arquivo_entrada.open(mode="r", encoding="utf-8") as f:
        leitor = csv.reader(f, delimiter=";")
        cabecalho = next(leitor) 

        for linha in leitor:
            produto = linha[0]
            quantidade = int(linha[1])
            preco = float(linha[2])
            total = quantidade * preco

            if total > 1000:
                destaques.append([produto, str(quantidade), f"{preco:.2f}", f"{total:.2f}"])

    with arquivo_saida.open(mode="w", newline="", encoding="utf-8") as f:
        escritor = csv.writer(f, delimiter=";")
        escritor.writerows(destaques)

    print(f"Relatório filtrado gerado com {len(destaques) - 1} itens em: {arquivo_saida}")
