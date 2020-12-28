"""
Crie um programa que leia a idade e o sexo de várias pessoas. A cada pessoa cadastrada, o programa deverá perguntar se
o usuário quer ou não continuar. No final, mostre:
A) Quantas pessoas tem mais de 18 anos.
B) Quantos homens foram cadastrados.
C) Quantas mulheres tem menos de 20 anos.
"""
print("=" * 7 + "FIM DO PROGRAMA" + "=" * 7)
print("-" * 32)
maior_18 = 0
homens = 0
mulher_menor_20 = 0
while True:
    print(f"{'CADASTRE UMA PESSOA': ^32}")
    print("-" * 32)
    idade = int(input("Idade: "))
    sexo = " "
    while sexo not in "MF":
        sexo = str(input("Sexo: [M/F] ")).strip().upper()
    if idade >= 18:
        maior_18 += 1
    if sexo in "M":
        homens += 1
    if sexo in "F" and idade < 20:
        mulher_menor_20 += 1
    resposta = " "
    while resposta not in "SN":
        resposta = str(input("Quer continuar? [S/N]")).strip().upper()
    if resposta == "N":
        break
print("=" * 7 + "FIM DO PROGRAMA" + "=" * 7)
print(f"Total de pessoas com mais de 18 anos: {maior_18}")
print(f"Ao todo temos {homens} homens cadastrados")
print(f"E temos {mulher_menor_20} mulheres com menos de 20 anos")
