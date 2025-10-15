print("==Maior Menor Numero==")
print()

maior = None
menor = None

for i in range(1, 6):
    num = float(input(f"Digite o {i}º número: "))
    
    if maior is None or num > maior:
        maior = num
    if menor is None or num < menor:
        menor = num

print("Maior valor:", maior)
print("Menor valor:", menor)
