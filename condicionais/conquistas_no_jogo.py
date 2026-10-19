partidas_jogadas = int(input("\nDigite quantas partidas você jogou: "))
partidas_ganhas = int(input("Digite quantas partidas você ganhou: "))

if partidas_jogadas <= 0:
    print("\nNúmero de partidas inválido.")
elif partidas_ganhas > partidas_jogadas or partidas_ganhas < 0:
    print("\nVerifique suas vitórias.") 
else:
    taxa_de_vitoria = (partidas_ganhas / partidas_jogadas) * 100

    if partidas_jogadas >= 100 and taxa_de_vitoria > 70:
        print(f"\nLenda! Seu aproveitamento é de {taxa_de_vitoria:.1f}%.")
    elif partidas_jogadas >= 50 and taxa_de_vitoria > 50:
        print(f"\nCompetidor! Seu aproveitamento é de {taxa_de_vitoria:.1f}%.")
    elif partidas_jogadas >= 10:
        print(f"\nIniciante. Seu aproveitamento é de {taxa_de_vitoria:.1f}%.")
    else:
        print("\nDesfrute mais do jogo para ganhar conquistas.")
