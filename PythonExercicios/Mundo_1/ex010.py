"""
Crie um programa que leia quanto dinheiro uma pessoa tem na carteira e mostre quantos Dólares ela pode comprar
"""

real = float(input("Digite quanto dinheiro você tem na carteira para saber quantos Dólares você pode comprar: R$"))
dolares = real / 5.07
print("Com R${:.2f} você pode comprar US${:.2f}".format(real, dolares))
