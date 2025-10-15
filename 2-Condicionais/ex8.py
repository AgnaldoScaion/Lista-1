print("==Calculadora Simples==")
print()

num1 = float(input("Digite o primeiro número: "))
num2 = float(input("Digite o segundo número: "))
operador = input("Digite o operador (+, -, *, /): ")

if operador == '+':
    resultado = num1 + num2
elif operador == '-':
    resultado = num1 - num2
elif operador == '*':
    resultado = num1 * num2
elif operador == '/':
    resultado = num1 / num2 if num2 != 0 else "Erro: divisão por zero"
else:
    resultado = "Operador inválido"

print("Resultado:", resultado)
