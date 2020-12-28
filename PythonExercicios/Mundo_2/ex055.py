"""
Faça um programa que leia o peso de cinco pessoas. No final, mostre qual foi o maior e o menor peso lidos.
"""
"""
peso = float(input("Digite o seu peso 1/5: "))
menor = peso
maior = peso
for pessoa in range(2, 6):
    peso = float(input("Digite o seu peso {}/5: ".format(pessoa)))
    if peso < menor:
        menor = peso
    if peso > maior:
        maior = peso
print("O menor peso foi de {}".format(menor))
print("O maior peso foi de {}".format(maior))
"""
maior = 0
menor = 0
for pessoa in range(1, 6):
    peso = float(input("Digite o seu peso {}/5: ".format(pessoa)))
    if pessoa == 1:
        maior = peso
        menor = peso
    else:
        if peso < menor:
            menor = peso
        if peso > maior:
            maior = peso
print("O menor peso foi de {}Kg".format(menor))
print("O maior peso foi de {}Kg".format(maior))
