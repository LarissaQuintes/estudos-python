peso_do_usuario = float(input("Digite seu peso (kg): ").replace(",", "."))
altura_do_usuario = float(input("Digite sua altura (m): ").replace(",", "."))
imc = peso_do_usuario /( altura_do_usuario ** 2)
print(f"Seu IMC: {imc:.2f}")

if imc < 18.5:
    print("Você está abaixo do peso.")
elif imc < 25 :
    print("Peso normal.")
else:
    print("Acima do peso.")