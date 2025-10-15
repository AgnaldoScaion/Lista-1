print("==Inversão de Vetor==")
print()

numeros = []

for i in range(7):
    num = int(input(f"Digite o {i+1}º número: "))
    numeros.append(num)

invertida = list(reversed(numeros))

print("Lista original:", numeros)
print("Lista invertida:", invertida)
