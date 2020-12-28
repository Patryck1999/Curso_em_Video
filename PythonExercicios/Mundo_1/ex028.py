"""
Escreva um programa que faça o computador "pensar" em um número inteiro entre 0 e 5 e peça para o usuário tentar
descobrir qual foi o número escolhido pelo computador.
OBS: O programa deverá escrever na tela se o usuário venceu ou perdeu.
"""
from random import randint
from time import sleep

numero = int(input("Digite um número de 0 a 5 em que você acha que será sorteado: "))
sorteio = randint(0, 5)
print("Processando...")
sleep(3)
if numero == sorteio:
    print("Parabéns o número {} foi sorteado. Você venceu!".format(numero))
else:
    print("Infelizmente o número sorteado foi {}. Você perdeu!".format(sorteio))
