"""
Refaça o DESAFIO 051, lendo o primeiro termo e a razão de uma PA, mostrando os 10 primeiros termos da progressão usando
a estrutura while.
"""
primeiro_termo = int(input("Digite o primeiro termo: "))
razao = int(input("Digite a razão: "))
contador = 1
acumulador = primeiro_termo
while contador <= 10:
    print(acumulador, end="->")
    acumulador += razao
    contador += 1
print("Fim")
