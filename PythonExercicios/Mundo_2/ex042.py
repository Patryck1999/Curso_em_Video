"""
Refaça o DESAFIO 035 dos triangulos, acrescentando o recurso de mostrar que tipo de triângulo será formado:
- Equilátero: todos os lados iguais
- Isosceles: dois lados iguais
- Escaleno: todos os lados diferentes
"""

reta_1 = float(input("Digite o valor da primeira reta: "))
reta_2 = float(input("Digite o valor da segunda reta: "))
reta_3 = float(input("Digite o valor da terceira reta: "))

if reta_1 < (reta_2 + reta_3) and reta_2 < (reta_1 + reta_3) and reta_3 < (reta_1 + reta_2):
    print("É possivel formar um triangulo!")
    if reta_1 == reta_2 == reta_3:
        print("Triângulo equilatero, pois todos os lados são iguais!")
    elif reta_1 != reta_2 == reta_3 or reta_2 != reta_1 == reta_3 or reta_3 != reta_1 == reta_2:
        print("Triângulo isosceles, pois pelo menos dois dos lados são iguais!")
    elif reta_1 != reta_2 != reta_3 != reta_1:
        print("Triângulo escaleno, pois todos os lados do triâgulo são diferentes!")
else:
    print("Não é possivel formar um triângulo")
