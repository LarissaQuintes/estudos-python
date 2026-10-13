while True:
    try:
        numero = int(input("Digite um número inteiro: "))
        break
    except ValueError:
        print("Digite um número inteiro!")

if numero % 2 == 0:
    print("O número é par!")
else:
    print("O número é ímpar!")