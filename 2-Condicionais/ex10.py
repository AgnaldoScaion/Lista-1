print("==Login==")
print()

usuario = input("Usuário: ")
senha = input("Senha: ")

if usuario == "admin" and senha == "1234":
    print("Acesso permitido!")
else:
    print("Acesso negado!")
