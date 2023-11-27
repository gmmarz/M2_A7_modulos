def escolha_jogador(possibilidades):
    while True:
        escolha = input("Escolha uma opção ['pedra', 'papel', 'tesoura']: ").lower()

        if escolha not in opcoes:
            print("Escolha inválida! Tente novamente.")
        else: 
            return escolha
        
def verificar_vencedor(jogador, computador):
    if jogador == computador:
        return "Empate"
    elif (jogador == "pedra" and computador == "tesoura") or \
        (jogador == "papel" and computador == "pedra") or \
        (jogador == "tesoura" and computador == "papel"):
        return "Você venceu!"
    else:
        return "A maquina venceu!"