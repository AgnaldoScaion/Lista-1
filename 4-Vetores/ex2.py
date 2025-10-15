print("==Soma, Média, Maior e Menor Valor==")
print()

numeros = []

for i in range(6):
    num = float(input(f"Digite o {i+1}º número: "))
    numeros.append(num)

soma = sum(numeros)
media = soma / len(numeros)
maior = max(numeros)
menor = min(numeros)

print(f"Soma: {soma}")
print(f"Média: {media:.2f}")
print(f"Maior valor: {maior}")
print(f"Menor valor: {menor}")
