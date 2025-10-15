print("==Leitura e Exibição de Elementos==")
print()

numeros = []

for i in range(5):
    num = int(input(f"Digite o {i+1}º número: "))
    numeros.append(num)

print("Números digitados:", numeros)
