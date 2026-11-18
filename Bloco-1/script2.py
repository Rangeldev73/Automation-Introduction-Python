pessoas = []

quantidade = int(input("QUANTAS PESSOAS DESEJA CADASTRAR? "))

for i in range(quantidade):
    print(f"\n--- CADASTRO {i + 1} ---")
    nome = input("INSIRA O NOME: ")
    idade = int(input("INSIRA A IDADE: "))
    altura = float(input("INSIRA A ALTURA: "))
    pessoas.append([nome, idade, altura])

print("\n--- LISTA DE CADASTRADOS ---")
for pessoa in pessoas:
    print(f"NOME: {pessoa[0]} && IDADE: {pessoa[1]} && ALTURA: {pessoa[2]}")