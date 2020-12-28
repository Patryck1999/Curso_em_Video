"""
Faça um programa que mostre a tabuada de vários números, um de cada vez, para cada valor digitado pelo usuário.
O programa será interrompido quando o número solicitado for negativo.
"""
"""
contador = 1
while True:
    numero = int(input("Quer ver a tabuada de qual valor? "))
    if numero < 0:
        break
    while contador <= 10:
        multiplicacao = numero * contador
        print(f"{numero} x {contador} = {multiplicacao}")
        contador += 1
print("PROGRAMA TABUADA ENCERRADA. Volte sempre!")
"""
while True:
    n = int(input("Quer ver a tabuada de qual valor? "))
    print("-" * 30)
    if n < 0:
        break
    for c in range(1, 11):
        print(f"{n} x {c} = {n * c}")
    print("-" * 30)
print("PROGRAMA TABUADA ENCERRADO. Volte sempre!")
