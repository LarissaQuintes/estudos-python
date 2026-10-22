horario_do_usuario = int(input("Digite o horário para verificação: "))

if 9 <= horario_do_usuario < 12 or 14 <= horario_do_usuario < 18:
    print("aberta")
elif horario_do_usuario == 12 or horario_do_usuario == 18:
    print("fechando agora")
elif horario_do_usuario < 0 or horario_do_usuario > 23:
    print("hora inválida")
else:
    print("fechada")