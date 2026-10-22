senha = input("Crie sua senha: ")

if len(senha) < 8:
    print("senha fraca. Essa tentativa tem poucos caracteres.")
elif senha == "12345678" or senha == "senha123":
    print("senha fraca. Essa tentativa é muito óbvia.")
else:
    print("senha forte")