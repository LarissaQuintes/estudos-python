player1 = input("player1: Qual sua escolha(pedra/papel/tesoura): ").lower()
player2 = input("player2: Qual sua escolha(pedra/papel/tesoura): ").lower()

if player1 != "pedra" and player1 != "papel" and player1 != "tesoura":
    print(f"inválido, player 1 escreveu {player1}")
elif player2 != "pedra" and player2 != "papel" and player2 != "tesoura":    
    print(f"inválido, player 2 escreveu {player2}")
elif (player1 == "papel" and player2 == "tesoura")  or (player1 == "pedra" and player2 == "papel") or (player1 == "tesoura" and player2 == "pedra") :
    print("Player2 ganhou")
elif (player2 == "papel" and player1 == "tesoura") or (player2 == "pedra" and player1 == "papel") or (player2 == "tesoura" and player1 == "pedra"):
    print("Player1 ganhou")
else: 
    print("Empate") 