idade = int(input("Digite a sua idade: "))

if 0 <= idade <= 11:
    print("Infantil")
elif 12 <= idade <= 17:
    print("Adolecente")
elif 18 <= idade <= 59:
    print("Adulto")
elif 60 <= idade <= 120:
    print("Idoso")
else:
    print("Idade inválida")
