"""
Faça um programa que mostre na tela uma contagem regressiva para estouro de fogos de artifício, indo de 10 até 0, com
uma pausa de 1 segundo entre eles.
"""
from time import sleep
inicio = 10
final = 0
print("-=" * 16)
print("Contagem regressiva iniciando!!")
print("-=" * 16)

for numero in range(inicio, final - 1, -1):
    sleep(1)
    print(numero)
sleep(1)
print("Bummmmmmm!")
