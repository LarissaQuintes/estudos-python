renda_mensal = float(input("Digite o valor da sua renda mensal: ").replace(",", "."))
valor_da_parcela = float(input("Digite o valor da parcela desejada: ").replace(",", "."))
limite_parcela = renda_mensal * 0.30

if renda_mensal <= 2000:
    print("Empréstimo negado: renda abaixo do mínimo.")
elif valor_da_parcela > limite_parcela:
    print("Empréstimo negado: parcela acima de 30% da renda.")
else:
    print("Empréstimo aprovado!")
