print("==Operadores Lógicos==")
print()

A = input("Digite o valor de A (True/False): ")
B = input("Digite o valor de B (True/False): ")
C = input("Digite o valor de C (True/False): ")
D = input("Digite o valor de D (True/False): ")

A = A == "True"
B = B == "True"
C = C == "True"
D = D == "True"

print("A and B:", A and B)
print("C and D:", C and D)
print("A and B and C:", A and B and C)
print("A and B and C and D:", A and B and C and D)
print("(A and B) and (C and D):", (A and B) and (C and D))
