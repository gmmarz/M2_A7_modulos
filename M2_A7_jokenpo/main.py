#Gabarito do professor.
import random
# import jogo #import todo do módulo jogo e salva na variável jogo
# from jogo import escolha_jogador, verificar_vencedor #Dessa forma a função fica acessível no código sem precisar estrever jogo.escolha_jogador.
#Atalho - ctrl + espaço - o VS Code mostrará as funções dentro do arquivo jogo.
#é possível também trazer todos os arquivos.
from jogo import *
from Utilidades.calculo import triplica
# from Utilidades import calculo

# num = triplica(3)
# print(num)


opcoes = ("pedra", "papel", "tesoura")

controle = True
while controle:
    escolha_computador = random.choice(opcoes)

    jogada = escolha_jogador(opcoes)

    print(f"A maquina escolheu: {escolha_computador}")

    resultado = verificar_vencedor(jogada, escolha_computador)
    print(resultado)

    resposta = input("Você quer continuar? [S/N] ").lower()

    if resposta == "n":
        controle = False
