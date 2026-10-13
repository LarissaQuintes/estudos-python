while True:
    try:
        nota_1 = float(input("Digite a primeira nota: ").replace(",", "."))
        if 0 <= nota_1 <= 10:
            break
        else:
            print("A nota precisa estar entre 0 e 10.")
    except ValueError:
        print("Isso não é um número! Tente de novo.")
while True:
    try:
        nota_2 = float(input("Digite a segunda nota: ").replace(",", "."))
        if 0 <= nota_2 <= 10:
            break
        else:
            print("A nota precisa estar entre 0 e 10.")
    except ValueError:
        print("Isso não é um número! Tente de novo.")
while True:
    try:
        nota_3 = float(input("Digite a terceira nota: ").replace(",", "."))
        if 0 <= nota_3 <= 10 :
            break
        else:
            print("A nota precisa estar entre 0 e 10.")
    except ValueError:
        print("Isso não é um número! Tente de novo.")

media_final = (nota_1 + nota_2 + nota_3) / 3

if media_final >= 7:
    print("Aprovado!")
elif 5 <= media_final < 7:
    print("Recuperação!")
else:
    print("Reprovado!")
print(f"Sua média é: {media_final:.2f}")
