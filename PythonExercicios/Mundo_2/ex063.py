"""
Escreva um programa que leia um número n inteiro qualquer e mostre na tela os n primeiros elementos de uma Sequência
de Fibonacci
"""
"""
numero = int(input("Digite um número para saber a sequencia de fibonnaci: "))
contador = 0
lista = []
while contador < numero:
    if len(lista) < 2:
        lista.append(contador)
        contador += 1
    else:
        lista.append(lista[contador - 2] + lista[contador - 1])
        contador += 1
fibonacci = str(lista).replace(',', ' ->').strip('[]')
print(fibonacci)
"""

print("-" * 30)
print("Sequencia de Fibonacci")
print("-" * 30)
n = int(input("Quantos termos você quer mostrar? "))
t1 = 0
t2 = 1
print("~" * 30)
print("{} -> {}".format(t1, t2), end="")
cont = 3
while cont <= n:
    t3 = t1 + t2
    print(" -> {}".format(t3), end="")
    t1 = t2
    t2 = t3
    cont += 1
print("-> FIM")
