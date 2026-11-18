from pathlib import Path

pasta_atual = Path.cwd()
print(f"Pasta atual: {pasta_atual}\n")

print("--- ITENS NA RAIZ DO PROJETO ---")
for item in pasta_atual.iterdir():
    tipo = "Pasta" if item.is_dir() else "Arquivo"
    print(f"[{tipo}] {item.name}")

pasta_bloco1 = pasta_atual / "Bloco-1"

if pasta_bloco1.exists():
    print("\n--- DETALHES DOS ARQUIVOS DO BLOCO 1 ---")
    for arquivo in pasta_bloco1.iterdir():
        print(f"Nome completo: {arquivo.name}")
        print(f"Apenas nome:   {arquivo.stem}")
        print(f"Extensão:      {arquivo.suffix}\n")
