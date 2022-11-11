import random
while 1:
    options = ["Pedra", "Papel", "Tesoura"]
    computer = random.choice(options)
    player = input("""
Escolha uma opção:
                   
Pedra
Papel
Tesoura

Sua escolha: """)
    print()
    print()
    print("=-="*14)
    print("                 Battle!")
    print("=-="*14)
    print(f"Computer --> {computer} vs {player} <-- Player")
    print()

    if (computer == "Pedra" and player == "Tesoura") or (computer == "Papel" and player == "Pedra") or (computer == "Tesoura" and player == "Papel"):
        print("Computer Wins!")
    elif computer == player:
        print("Draw!")
    else:
        print("You Win!")
    print()
    print("=-="*25)