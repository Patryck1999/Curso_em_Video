"""
Faça um programa que leia um número inteiro e diga se ele é ou não um número primo
"""
"""
numero = int(input("Digite um número e verifique se ele é ou não primo: "))
contador = 0
resultado = ""
for valor in range(1, numero + 1):
    if numero % 1 == 0 and numero % valor == 0:
        contador += 1
        if contador == 2:
            resultado = "Primo"
        else:
            resultado = "Não primo"
print(resultado)
"""
num = int(input("Digite um número e verifique se ele é ou não primo: "))
tot = 0
for c in range(1, num + 1):
    if num % c == 0:
        print("\033[33m", end=" ")
        tot += 1
    else:
        print("\033[31m", end=" ")
    print("{}".format(c), end=" ")
print("\n\033[mO número {} foi divisível {} vezes".format(num, tot))
if tot == 2:
    print("E por isso ele é PRIMO!")
else:
    print("E por isso ele não é PRIMO!")