"""
Crie um programa que leia vários números inteiros pelo teclado. O programa só vai parar quando o usuário digitar
o valor 999, que é a condição de parada. No final, mostre quantos números foram digitados e qual foi a soma entre eles.
OBS: Desconsiderando o flag
"""
contador = soma = 0
while True:
    numero = int(input("Digite um valor (999 para parar): "))
    if numero == 999:
        break
    soma += numero
    contador += 1
print(f"A soma dos {contador} valores foi {soma}")
