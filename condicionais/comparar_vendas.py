bananas_vendidas = int(input("Digite a quantidade de bananas vendidas: "))
macas_vendidas = int(input("Digite a quantidade de maças vendidas: "))

if bananas_vendidas > macas_vendidas:
    print("As bananas tiveram mais vendas")
elif bananas_vendidas == macas_vendidas:
    print("As bananas e as maças tiveram as mesmas quantidades de vendas")
else:
    print("As maças tiveram mais vendas")