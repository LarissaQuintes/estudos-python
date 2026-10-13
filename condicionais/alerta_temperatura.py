temperatura_atual = float(input("Digite a temperatura atual: ").replace(",", "."))
temperatura_limite = 25

if temperatura_atual < temperatura_limite:
    print("Ótima notícia! Temperatura está abaixo do limite.")
elif temperatura_atual == temperatura_atual:
    print("Atenção! Temperatura está no limite máximo.")
else:
    print("Alerta! Temperatura acima do limite permitido.")