"""
Faça um programa que leia o ano de nascimento de um jovem e informe, de acordo com sua idade:
- Se ele ainda vai se alistar ao serviço militar.
- Se é a hora de se alistar.
- Se já passou do tempo do alistamento.
OBS: Seu programa também deverá mostrar o tempo que falta ou que passou do prazo
"""
from datetime import date
atual = date.today().year
ano = int(input("Digite o ano do seu nascimento: "))
idade = atual - ano

if idade < 18:
    tempo = 18 - idade
    print("Você tem {} anos, ainda não chegou a sua hora de se alistar, ainda falta {} anos!".format(idade, tempo))
    ano = atual + tempo
    print("Seu alistamento será em {}".format(ano))
elif idade == 18:
    print("Você tem {} anos,a sua hora de se alistar chegou!, faça já o seu alistamento!".format(idade))
else:
    tempo = idade - 18
    print("Você tem {} anos, o seu tempo de alistamento já passou, isso já se passou {} anos".format(idade, tempo))
    ano = atual - tempo
    print("Seu alistamento foi em {}".format(ano))
