"""
O mesmo professor do desafio anterior quer sortear a ordem de apresentação de trabalhos dos alunos. Faça um programa
que leia o nome dos quatro alunos e mostre a ordem sorteada.
"""
"""
from random import randint

aluno_1 = input("Digite o nome do primero aluno: ")
aluno_2 = input("Digite o nome do segundo aluno: ")
aluno_3 = input("Digite o nome do terceiro aluno: ")
aluno_4 = input("Digite o nome do quarto aluno: ")
lista = [aluno_1, aluno_2, aluno_3, aluno_4]

sorteio = randint(0, 3)
print("O primeiro aluno a apresentar é {}".format(lista[sorteio]))
lista.remove(lista[sorteio])

sorteio = randint(0, 2)
print("O segundo aluno a apresentar é {}".format(lista[sorteio]))
lista.remove(lista[sorteio])

sorteio = randint(0, 1)
print("O terceiro aluno a apresentar é {}".format(lista[sorteio]))
lista.remove(lista[sorteio])

sorteio = randint(0, 0)
print("O quarto aluno a apresentar é {}".format(lista[sorteio]))
lista.remove(lista[sorteio])
"""
from random import shuffle

aluno_1 = input("Primeiro aluno: ")
aluno_2 = input("Segundo aluno: ")
aluno_3 = input("Terceiro aluno: ")
aluno_4 = input("Quarto aluno: ")
lista = [aluno_1, aluno_2, aluno_3, aluno_4]
shuffle(lista)
print("A ordem de apresentação será ")
print(lista)
