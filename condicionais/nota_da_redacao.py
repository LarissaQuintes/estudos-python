nota_da_redacao = int(input("Digite a nota da sua redação (0 a 1000): "))

if nota_da_redacao < 0 or nota_da_redacao > 1000:
    print("nota inválida")
elif nota_da_redacao < 600:
    print("nota insuficiente")
elif nota_da_redacao < 900:
    print("nota boa")
else:
    print("nota execelente")