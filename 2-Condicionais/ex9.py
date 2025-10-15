print("==Categoria de idade==")
print()

idade = int(input("Digite a idade: "))

if idade < 12:
    categoria = "Criança"
elif idade <= 17:
    categoria = "Adolescente"
elif idade <= 59:
    categoria = "Adulto"
else:
    categoria = "Idoso"

print("Categoria:", categoria)
