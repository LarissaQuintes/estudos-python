idade_do_usuario = int(input("Digite sua idade: "))
dia_da_semana = int(input("Digite o dia da semana(1 a 7): "))
estudante = input("Você é estudante(s/n): ").lower()

if dia_da_semana < 1 or dia_da_semana > 7 or idade_do_usuario < 0:
    print("Invalido!")
else:
    if dia_da_semana == 3:
        preco = 20
    else:
        preco = 30

    if idade_do_usuario < 18 or idade_do_usuario > 60 or estudante == "s":
        preco = preco / 2
    print(f"Valor do ingresso: R$ {preco:.2f}")
