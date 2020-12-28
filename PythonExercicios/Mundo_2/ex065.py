"""
Crie um programa que leia vários números inteiros pelo teclado. No final da execução, mostre a média entre todos os
valores e qual foi o maior e o menor valores lidos. O programa deve perguntar ao usuário se ele quer ou não continuar
a digitar valores.
"""
maior = 0
menor = 0
soma = 0
media = 0
contador = 0
resposta = ''
while resposta != 'N':
    valor = int(input("Digite um valor: "))
    soma += valor
    contador += 1
    if contador == 1:
        maior = valor
        menor = valor
    else:
        if valor > maior:
            maior = valor
        elif valor < menor:
            menor = valor
    resposta = input("Deseja continuar? S/N: ").upper().strip()[0]
media = soma / contador
print("O maior número digitado foi {}".format(maior))
print("O menor número digitado foi {}".format(menor))
print("A média entre os {} números digitados foram: {}".format(contador, media))
