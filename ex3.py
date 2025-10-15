print("==Operador Módulo==")
print()

num = int(input("Digite um número inteiro: "))

resto2 = num % 2
resto3 = num % 3
resto5 = num % 5
resto10 = num % 10

print("=== Resultados das divisões ===")
print("Resto da divisão por 2:", resto2)
print("Resto da divisão por 3:", resto3)
print("Resto da divisão por 5:", resto5)
print("Resto da divisão por 10:", resto10)

if resto2 == 0:
    print("O número", num, "é PAR.")
else:
    print("O número", num, "é ÍMPAR.")
