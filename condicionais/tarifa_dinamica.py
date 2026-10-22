kilometros = float(input("Digite o Km da corrida: ").replace(",","."))
horario = int(input("Digite o horário da corrida: "))
tempo_atual = input("Está chovendo? (s/n): ")
corrida_minima = 8 

if kilometros <= 0:
    print("É necessário que km seja válido")
elif horario < 0 or horario > 23:
    print("Esse horário não existe")
elif tempo_atual != "s" and tempo_atual != "n":
    print("responda apenas com s ou n")
else:
    taxa_com_km = 2 * kilometros
    
    if 17 <= horario <= 19 and tempo_atual == "s":
        valor_da_corrida = taxa_com_km * 1.80
    elif 17 <= horario <= 19 or tempo_atual == "s":
        valor_da_corrida = taxa_com_km * 1.50
    else:
        valor_da_corrida = taxa_com_km

    if valor_da_corrida < corrida_minima:
        valor_da_corrida = corrida_minima
        
    print(f"valor da corrida: R${valor_da_corrida:.2f}")