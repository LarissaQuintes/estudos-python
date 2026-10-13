horario_atual = int(input("Digite a hora atual (formato 24 horas): "))
horario_maximo = 18
horario_minimo = 8


if horario_atual < 0 or horario_atual >= 24:
    print("Esse horário não existe")
elif horario_minimo <= horario_atual < horario_maximo:
    print("Acesso liberado.")
else:
    print("Acesso negado.")
