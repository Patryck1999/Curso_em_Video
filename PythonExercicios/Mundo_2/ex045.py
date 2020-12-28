"""
Crie um programa que faça o computador jogar Jokenpô com você.
"""
"""
from random import choice
from time import sleep

pedra = "\U0001F44A"
papel = "\U0001F9FB"
tesoura = "\U00002704"
sorteio = [pedra, papel, tesoura]
print('-=' * 10)
print('1 - pedra')
print('2 - papel')
print('3 - tesoura')
print('-=' * 10)
opcao = int(input("Escolha uma opção para jogar pedra papel tesoura: "))
adversario = choice(sorteio)
print("JO")
sleep(1)
print("KEN")
sleep(1)
print("PO!!")
sleep(1)
print("Adversario {} x {} você".format(adversario, sorteio[opcao-1], end=""))
print()
if opcao == 1:
    if adversario == sorteio[0]:
        print("Empate!!!")
    elif adversario == sorteio[1]:
        print("Você perdeu!!!")
    else:
        print("Você ganhou!!!")
elif opcao == 2:
    if adversario == sorteio[1]:
        print("Empate!!!")
    elif adversario == sorteio[2]:
        print("Você perdeu!!!")
    else:
        print("Você ganhou!!!")
elif opcao == 3:
    if adversario == sorteio[2]:
        print("Empate!!!")
    elif adversario == sorteio[0]:
        print("Você perdeu!!!")
    else:
        print("Você ganhou!!!")
else:
    print("Opção Invalida")
"""

from random import randint
from time import sleep
itens = ('Pedra', 'Papel', 'Tesoura')
computador = randint(0, 2)
print("""Sua opções
[ 0 ] Pedra
[ 1 ] Papel
[ 2 ] Tesoura""")

jogador = int(input("Qual é a sua jogada? "))
print("JO")
sleep(1)
print("KEN")
sleep(1)
print("PO!!")
sleep(1)
print("-=" * 11)
print("Computador jogou {}".format(itens[computador]))
print("Jogador jogou {}".format(itens[jogador]))
print('-=' * 11)
if computador == 0:
    if jogador == 0:
        print("EMPATE")
    elif jogador == 1:
        print("JOGADOR VENCE")
    elif jogador == 2:
        print("COMPUTADOR VENCE")
    else:
        print("JOGADA INVÁLIDA!")
elif computador == 1:
    if jogador == 0:
        print("COMPUTADOR VENCE")
    elif jogador == 1:
        print("EMPATE")
    elif jogador == 2:
        print("JOGADOR VENCE")
    else:
        print("JOGADA INVÁLIDA!")
elif computador == 2:
    if jogador == 0:
        print("JOGADOR VENCE")
    elif jogador == 1:
        print("COMPUTADOR VENCE")
    elif jogador == 2:
        print("EMPATE")
    else:
        print("JOGADA INVÁLIDA")

