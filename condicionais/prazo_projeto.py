atividade_A = int(input("Informe os dias para a atividade A: "))
ativadade_B = int(input("Informe os dias para a atividade B: "))
atividade_C = int(input("Informe os dias para a atividade C: "))

if  atividade_A >= 0 and ativadade_B >= 0 and atividade_C >= 0:
    tempo_total = atividade_A + ativadade_B + atividade_C
    print(f"tempo total do projeto: {tempo_total} dias")
else:
    print("Erro: Os dias não podem ser negativos, Verifique!")