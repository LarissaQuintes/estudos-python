login = input("Digite seu login: ")
senha = input("Digite sua senha: ")

if login == "admin" and senha != "1234":
    print("senha incorreta")
elif login == "admin" and senha == "1234":
    print("acesso liberado")
else:
    print("usuário não encontrado")