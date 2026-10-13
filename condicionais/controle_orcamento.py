limite_para_gastos = 3000.0
despesas_mes = float(input("Digite o total de despesas do mês (R$): ").replace(",", "."))
calculo_despesas = limite_para_gastos - despesas_mes

if despesas_mes > limite_para_gastos:
    print("Atenção! Você ultrapassou o limite do orçamento.")
    print(f"Saldo: R${calculo_despesas:.2f}") 
elif despesas_mes == limite_para_gastos:
    print("Você atingiu exatamente o limite do orçamento.")
else:
    print("Você ainda tem limite para gastar")
    print(f"Parabéns! Sobrou R$: {calculo_despesas:.2f}")