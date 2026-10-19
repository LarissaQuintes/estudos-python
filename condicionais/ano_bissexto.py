ano_do_usuario = int(input("Digite o ano para verificação: "))

if ano_do_usuario <= 0:
    print("Inválido.")
elif (ano_do_usuario % 4 == 0 and ano_do_usuario % 100 != 0) or ano_do_usuario % 400 == 0:
    print("ano bissexto.")
else:
    print("ano não bissexto.")


