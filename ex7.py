print("==Operador Lógico NOT==")
print()

A = input("Digite o valor de A (True/False): ")
B = input("Digite o valor de B (True/False): ")
C = input("Digite o valor de C (True/False): ")

A = A == "True"
B = B == "True"
C = C == "True"

print("not A:", not A)
print("not B:", not B)
print("not C:", not C)
print("not (A and B):", not (A and B))
print("not (A or B):", not (A or B))
print("not A and not B:", not A and not B)
print("not (not A):", not (not A))