"""
Um professor quer sortear um dos quatro alunos para apagar o quadro. Faça um programa que ajude ele, lendo o nome deles
e escrevendo o nome do escolhido.
"""
"""
from random import randint

aluno_1 = input("Digite o nome do primeiro aluno:")
aluno_2 = input("Digite o nome do segundo aluno: ")
aluno_3 = input("Digite o nome do terceiro aluno: ")
aluno_4 = input("Digite o nome do quarto aluno: ")
lista = [aluno_1, aluno_2, aluno_3, aluno_4]
sorteio = randint(0, 3)
print("Dos 4 alunos selecionados para apagar a lousa o sorteado foi: {}".format(lista[sorteio]))
"""""
from random import choice

aluno_1 = input("Digite o nome do primeiro aluno:")
aluno_2 = input("Digite o nome do segundo aluno: ")
aluno_3 = input("Digite o nome do terceiro aluno: ")
aluno_4 = input("Digite o nome do quarto aluno: ")
lista = [aluno_1, aluno_2, aluno_3, aluno_4]
sorteio = choice(lista)
print("O aluno escolhido foi {}".format(sorteio))
