print("==Operadores Calculaveis==")
print()
num1 = int(input("Insira um numero: "))
num2 = int(input("Insira outro numero: "))
print("Operações disponiveis")
print("soma | subtracao | multiplicacao | divisao | resto | potencia")
decisao = input("Como deseja calcular? ")

if decisao == "soma":
    resultado = num1 + num2
    print("A soma dos números foi", resultado)

elif decisao == "subtracao":
    resultado = num1 - num2
    print("A subtração dos números foi", resultado)

elif decisao == "multiplicacao":
    resultado = num1 * num2
    print("A multiplicação dos números foi", resultado)

elif decisao == "divisao":
    if num2 != 0:
        resultado = num1 / num2
        print("A divisão dos números foi", resultado)
    else:
        print("Erro: divisão por zero não permitida.")

elif decisao == "resto":
    if num2 != 0:
        resultado = num1 % num2
        print("O resto da divisão é", resultado)
    else:
        print("Erro: divisão por zero não é permitida.")

elif decisao == "potencia":
    resultado = num1 ** num2
    print(f"{num1} elevado a {num2} é: {resultado}")

else:
    print("Operação inválida.")
    