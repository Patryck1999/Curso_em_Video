"""
A confederação Nacional precisa de um programa que leia o ano de nascimento de um atleta e mostre sua categoria, de
acordo com a idade:
- Até 9 anos: Mirim
- Até 14 anos: Infantil
- Até 19 anos: Júnior
- Até 25 anos: Sênior
- Acima: Master
"""
from datetime import date
atual = date.today().year
ano_nascimento = int(input("Digite o seu ano de nascimento: "))
idade = atual - ano_nascimento
print("O atleta tem {} anos".format(idade))
if idade < 0:
    print("Digite um ano menor do que o atual para que no minímo a pessoa exista.")
elif idade <= 9:
    print("Mirim")
elif idade <= 14:
    print("Infantil")
elif idade <= 19:
    print("Junior")
elif idade <= 25:
    print("Sênior")
else:
    print("Master")
