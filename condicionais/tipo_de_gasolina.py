valor_da_gasolina = float(input("Digite o valor da gasolina: ").replace(",","."))
valor_do_alcool = float(input("Digite o valor do álcool: ").replace(",","."))
limite_alcool = valor_da_gasolina * 0.70

if valor_da_gasolina <= 0 and valor_do_alcool <= 0:
    print("Inválido! Os preços da gasolina e do álcool devem ser maiores que zero.")
elif valor_da_gasolina <= 0:
    print("Inválido! O preço da gasolina deve ser maior que zero.")
elif valor_do_alcool <= 0:
    print("Inválido! O preço do álcool deve ser maior que zero.")
elif valor_do_alcool <= limite_alcool: 
    print("Compensa!")
else:
    print("Não compensa! O valor do álcool ultrapassa 70% da gasolina.")