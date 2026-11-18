from pathlib import Path

pasta_atual = Path.cwd()
pasta_origem = pasta_atual / "pasta_origem"
pasta_destino = pasta_atual / "pasta_destino"

pasta_origem.mkdir(exist_ok=True)
pasta_destino.mkdir(exist_ok=True)

arquivo_origem = pasta_origem / "relatorio.txt"
arquivo_origem.write_text("Dados importantes do relatório.", encoding="utf-8")
print(f"Arquivo criado em: {arquivo_origem}")

arquivo_destino = pasta_destino / arquivo_origem.name

arquivo_origem.replace(arquivo_destino)

print(f"Arquivo movido com sucesso para: {arquivo_destino}")
