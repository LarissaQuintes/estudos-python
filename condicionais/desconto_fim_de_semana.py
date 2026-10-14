valor_compra = float(input("Digite o valor da compra: ").replace(",", "."))
dia_da_semana = int(input("Digite o dia da semana(1 = domingo, 7 = sábado): "))

desconto = valor_compra * 0.10
valor_com_desconto = valor_compra - desconto

if dia_da_semana < 1 or dia_da_semana > 7:
    print("inválido")
elif dia_da_semana == 1 or dia_da_semana == 7 or valor_compra > 500:
    print("Parabéns! Você ganhou um desconto de 10%")
    print(f"Valor total: R${valor_com_desconto:.2f} ")
else: 
    print(f"Valor total: R${valor_compra:.2f}")
