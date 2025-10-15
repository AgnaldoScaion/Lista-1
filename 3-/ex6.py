print("==Numeros de Repetição==")
print()

num = int(input("Digite um número: "))

if num < 2:
    print(f"O número {num} não é primo.")
else:
    primo = True
    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            primo = False
            break
    if primo:
        print(f"O número {num} é primo.")
    else:
        print(f"O número {num} não é primo.")
