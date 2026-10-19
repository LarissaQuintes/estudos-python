mes = int(input("Digite o número do mês que você deseja descobrir a estação do ano(1 a 12): "))

if mes < 1 or mes > 12:
    print("Inválido!")
else:
    if mes < 3 or mes == 12:
        print("verão")
    elif mes < 6:
        print("outono")
    elif mes < 9:
        print("inverno")  
    else: 
        print("primavera") 
