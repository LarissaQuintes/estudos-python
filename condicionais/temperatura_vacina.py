temperatura_atual = float(input("Digite a temperatura:  ").replace(",", "."))

if temperatura_atual < 2 or temperatura_atual > 8:
    print("Alerta!")
else:
    print("Temperatura adequada.")