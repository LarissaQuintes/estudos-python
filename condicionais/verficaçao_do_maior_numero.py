number1 = int(input("Digite o primeiro número: "))
number2 = int(input("Digite o segundo número: "))
number3 = int(input("Digite o terceiro número: "))

if number1 > number2 and number1 > number3:
    print(f"{number1} é maior que {number2} e {number3}")
elif number2 > number1 and number2 > number3:
    print(f"{number2} é maior que {number1} e {number3}")
elif number3 > number1 and number3 > number2:
    print(f"{number3} é maior que {number1} e {number2}")
elif number1 == number2 == number3:
    print("Todos os números são iguais")
else: 
    if number1 == number2: 
        print(f"{number1} e {number2} são iguais e maiores, já o {number3} é diferente")
    elif number2 == number3 :
        print(f"{number2} e {number3} são iguais e maiores, já o {number1} é diferente")
    else:
        print(f"{number1} e {number3} são iguais e maiores, já o {number2} é diferente")