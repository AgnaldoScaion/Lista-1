print("==Operador Lógico OR==")
print()

A = input("Digite o valor de A (True/False): ")
B = input("Digite o valor de B (True/False): ")
C = input("Digite o valor de C (True/False): ")
D = input("Digite o valor de D (True/False): ")

A = A == "True"
B = B == "True"
C = C == "True"
D = D == "True"

print("A or B:", A or B)
print("C or D:", C or D)
print("A or B or C:", A or B or C)
print("A or B or C or D:", A or B or C or D)
print("(A or B) or (C or D):", (A or B) or (C or D))
