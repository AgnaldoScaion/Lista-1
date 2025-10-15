print("==Pesquisa em Vetor==")
print()

nomes = []

for i in range(5):
    nome = input(f"Digite o {i+1}º nome: ")
    nomes.append(nome)

busca = input("Digite um nome para buscar: ")

if busca in nomes:
    print(f'O nome "{busca}" está na lista.')
else:
    print(f'O nome "{busca}" não está na lista.')
