"""
Melhore o jogo do DESAFIO 028 onde o computador vai "pensar" entre 0 e 10. Só que agora o jogador vai tentar adivinhar
até acertar, mostrando no final quantos palpites foram necessários para vencer.
"""
"""
from random import randint
from time import sleep
computador = randint(0, 10)
eu = int(input("O número que o computador pensou foi: "))
contador = 1
while eu != computador:
    sleep(1)
    contador += 1
    eu = int(input("Não, Tente outro número que você acha que o computador pensou: "))
sleep(1)
print("Sim, Foi preciso {} palpites para que você pudesse acertar.".format(contador))
print("O número sorteado foi {}".format(computador))
"""
from random import randint
computador = randint(0, 10)
print("Sou seu computador... Acabei de pensar em um número entre 0 e 10.")
print("Será que você consegue adivinhar qual foi?")
acertou = False
palpites = 0
while not acertou:
    jogador = int(input("Qual é seu palpite? "))
    palpites += 1
    if jogador == computador:
        acertou = True
    else:
        if jogador < computador:
            print("Mais... Tente mais uma vez")
        elif jogador > computador:
            print("Menos... Tente mais uma vez")
print("Acertou com {} tentativas. Parabéns!".format(palpites))

