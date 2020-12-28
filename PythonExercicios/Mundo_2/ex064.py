"""
Crie um programa que leia vários números inteiros pelo teclado. O programa só vai parar quando o usuário digitar o valor
999, que é a condição de parada. No final, mostre quantos números foram digitados e qual foi a soma entre eles
(desconsiderando o flag).
"""
"""
controle = 0
acumulador = 0
contador = 0
while controle != 999:
    numero = int(input("Digite um número: "))
    if numero == 999:
        controle = 999
        print("Fim do programa")
    else:
        acumulador += numero
        contador += 1
print("Foram somados {} numeros e a soma dos números é igual a {}".format(contador, acumulador))
"""

num = cont = soma = 0
num = int(input("Digite um número [999 para parar]: "))
while num != 999:
    soma += num
    cont += 1
    num = int(input("Digite um número [999 para parar]: "))
print("Você digitou {} números e a soma entre eles foi {}.".format(cont, soma))
