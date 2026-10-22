limite_da_via = 60
velocidade_do_usuario = int(input("Digite a velocidade do veículo(km/h): "))
limite_multa_leve = (limite_da_via * 0.20) + limite_da_via

if velocidade_do_usuario <= limite_da_via:
    print("dentro do limite")
elif velocidade_do_usuario <= limite_multa_leve:
    print("multa leve")
else:
    print("multa grave")
