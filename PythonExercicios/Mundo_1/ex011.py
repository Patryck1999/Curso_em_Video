"""
Faça um programa que leia a largura e a altura de uma parede em metros, calcule a sua área e a quantidade de tinta
necessária para pinta-la, sabendo que cada litro de tinta, pinta uma área de 2m2.
"""

largura = float(input("Digite a largura da parede: "))
altura = float(input("Digite a altura da parede:"))
area = largura * altura
litros = area / 2
print("Sua parede tem a dimensão de {}x{} e sua área é de {}m².".format(largura, altura, area))
print("Para pintar essa parede, você precisara de {}l de tinta.".format(litros))
