print("==Separação de Pares e Ímpares==")
print()

numeros = []
pares = []
impares = []

for i in range(10):
    num = int(input(f"Digite o {i+1}º número: "))
    numeros.append(num)
    if num % 2 == 0:
        pares.append(num)
    else:
        impares.append(num)

print("Todos os números:", numeros)
print("Números pares:", pares)
print("Números ímpares:", impares)
