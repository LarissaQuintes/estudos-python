renda_usuario = float(input("Digite sua renda mensal: ").replace(",", "."))
parcela_usuario = float(input("Qual o valor da parcela que você deseja: ").replace(",", "."))
limite_parcela = renda_usuario * 0.30 

if renda_usuario <= 2000 and parcela_usuario > limite_parcela :
    print("Reprovado! A renda precisa ser maior que R$ 2.000 e a parcela não pode passar de 30% da renda")
elif renda_usuario <= 2000:
    print("Reprovado! A renda precisa ser maior que R$ 2.000")
elif parcela_usuario > limite_parcela:
    print("Reprovado! A parcela não pode passar de 30% da renda")
else: 
    print("Aprovado!")