print("==Soma de numeros pares==")
print()

N = int(input("Digite um número: "))
soma = 0

for i in range(1, N + 1):
    if i % 2 == 0:
        soma += i

print("Soma dos números pares entre 1 e", N, ":", soma)
