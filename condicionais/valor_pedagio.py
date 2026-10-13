distancia_percorrida = float(input("Digite a distância percorrida (em km): ").replace(",", "."))

if distancia_percorrida < 0:
    print("Digite um número maior que zero")
elif distancia_percorrida <= 100:
    print("O valor do pedágio: R$ 10,00")
elif distancia_percorrida <= 200:
    print("O valor do pedágio: R$ 20,00")
else:
    print("O valor do pedágio: R$ 30,00")