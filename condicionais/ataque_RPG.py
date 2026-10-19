dado_do_usuario = int(input("\nDigite o número do lado do dado: "))
vida_do_adversario = int(input("\nDigite a quantidade de vida do adversário: "))

if dado_do_usuario < 1 or dado_do_usuario > 20:
    print("quantidade de lados não existe")
elif vida_do_adversario <= 0:
    print("Vida insuficente") 
else:
    if dado_do_usuario == 1:
        dano = 0
    elif dado_do_usuario < 20:
        dano = 20
    else:
        dano = 40

    print(f"\nDano causado {dano}")

    vida_restante = vida_do_adversario - dano

    if vida_restante <= 0:
        print("Inimigo derrotado!")
    else:
        print(f"O inimigo ainda tem {vida_restante} de vida.")


