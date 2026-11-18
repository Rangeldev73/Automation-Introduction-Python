from pathlib import Path

pasta_atual = Path.cwd()
pasta_arquivos = pasta_atual / "arquivos_para_renomear"
pasta_arquivos.mkdir(exist_ok=True)

nomes_baguncados = ["doc_final.txt", "anotacoes_aula.txt", "rascunho_v2.txt"]
for nome in nomes_baguncados:
    (pasta_arquivos / nome).write_text("Conteúdo de teste.", encoding="utf-8")

print("--- ANTES DE RENOMEAR ---")
for item in pasta_arquivos.iterdir():
    print(item.name)

print("\n--- RENOMEANDO ---")
arquivos_txt = sorted(pasta_arquivos.glob("*.txt"))

for indice, arquivo in enumerate(arquivos_txt, start=1):
    novo_nome = f"relatorio_{indice:02d}{arquivo.suffix}"
    novo_caminho = pasta_arquivos / novo_nome
    
    arquivo.replace(novo_caminho)
    print(f"{arquivo.name}  --->  {novo_nome}")
