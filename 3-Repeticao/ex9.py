print("==Contagem de impar e par==")
print()

pares = 0
impares = 0
soma = 0

for i in range(1, 11):
    num = int(input(f"Digite o {i}º número: "))
    soma += num
    if num % 2 == 0:
        pares += 1
    else:
        impares += 1

print("Pares:", pares)
print("Ímpares:", impares)
print("Soma total:", soma)
