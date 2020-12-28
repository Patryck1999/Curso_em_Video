"""
Crie um programa que simule o funcionamento de um caixa eletrônico. No inicio, pergunte ao usuário qual será o valor
a ser sacado(número inteiro) e o programa vai informar quantas cédulas de cada valor serão entregues.
OBS: Considere que o caixa possui cédulas de R$50, R$20, R$10 e R$1.
"""
"""
cedula_50 = 0
cedula_20 = 0
cedula_10 = 0
cedula_1 = 0
print("=" * 32)
print(f"{'BANCO CEV': ^32}")
print("=" * 32)
valor = int(input("Que valor você quer sacar? R$"))
while valor > 0:
    if valor % 50 == 0:
        cedula_50 += 1
        valor -= 50
    elif valor % 20 == 0:
        cedula_20 += 1
        valor -= 20
    elif valor % 10 == 0:
        cedula_10 += 1
        valor -= 10
    elif valor % 1 == 0:
        cedula_1 += 1
        valor -= 1
print(f"Total de {cedula_50} cédulas de R$50")
print(f"Total de {cedula_20} cédulas de R$20")
print(f"Total de {cedula_10} cédulas de R$10")
print(f"Total de {cedula_1} cédulas de R$1")
print("=" * 32)
"""
print("=" * 30)
print("{:^30}".format("BANCO CEV"))
print("=" * 30)
valor = int(input("Que valor você quer sacar? R$"))
total = valor
ced = 50
totced = 0
while True:
    if total >= ced:
        total -= ced
        totced += 1
    else:
        if totced > 0:
            print(f"Total de {totced} cédulas de R${ced}")
        if ced == 50:
            ced = 20
        elif ced == 20:
            ced = 10
        elif ced == 10:
            ced = 1
        totced = 0
        if total == 0:
            break
print("=" * 30)
print("Volte sempre ao BANCO CEV! Tenha um bom dia!")