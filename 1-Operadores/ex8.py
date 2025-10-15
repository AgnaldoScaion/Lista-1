print("==Operadores Racionais e Logicos==")
print()

x = float(input("Digite o valor de x: "))
y = float(input("Digite o valor de y: "))
z = float(input("Digite o valor de z: "))

# Avalia e exibe as expressões
print("x > y and y > z:", x > y and y > z)
print("x > y or y > z:", x > y or y > z)
print("x == y or x == z:", x == y or x == z)
print("x != y and y != z:", x != y and y != z)
print("not (x > y) and z > y:", not (x > y) and z > y)
print("(x > y and y > z) or (x == z):", (x > y and y > z) or (x == z))