"""Jogo de Craps. Faça um programa de implemente um jogo de Craps.
O jogador lança um par de dados, obtendo um valor entre 2 e 12.
Se, na primeira jogada, você tirar 7 ou 11, você um "natural" e ganhou.
Se você tirar 2, 3 ou 12 na primeira jogada, isto é chamado de "craps" e você perdeu.
Se, na primeira jogada, você fez um 4, 5, 6,8, 9 ou 10,este é seu "Ponto". 
Seu objetivo agora é continuar jogando os dados até tirar este número novamente.
Você perde, no entanto, se tirar um 7 antes de tirar este Ponto novamente."""

import random

def jogar_dado():
        return random.randint(1,6)

def craps():
    print("BEM VINDO AO JOGO CRAPS 🎲")
    
    
    dado1 = jogar_dado()
    dado2 = jogar_dado()
    soma = dado1 + dado2
    print(f"\nVocê rodou o dado 1 = {dado1} e o dado 2 = {dado2}  e a soma foi = {soma}")
    
    if soma in [7,11]:
        print(f"\nVocÊ ganhou!🍾")
    elif soma in [2,3,12]:
        print(f"\nVocê perdeu!💔")
    else:
        ponto = soma
        print(f"\nSeu ponto é {ponto}, continue jogando até tirar {ponto} novamente para ganhar, ou tirar 7 para perder.")

    while True:
        input("\nAperte enter para rolar os dados novamente!")
        dado1 = jogar_dado()
        dado2 = jogar_dado()
        soma = dado1 + dado2
        print(f"\nVocê rodou o dado 1 = {dado1} e o dado 2 = {dado2}  e a soma foi = {soma}")
        
        if soma == ponto:
            print(f"\nVocê acertou o ponto! Ganhou🏆")
        elif soma == 7:
            print("\nVoce tirou 7 antes do ponto. VocÊ PERDEU! Noob")
            break
        
craps()
