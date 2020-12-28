"""
Desenvolva um programa que leia o nome, idade e sexo de 4 pessoas. No final do programa, mostre:
- A média de idade do grupo.
- Qual é o nome do homem mais velho.
- Quantas mulheres têm menos de 20 anos.
"""
pessoas = 4
soma = 0
media = 0
contador_mulher = 0
homem_maior = {}
idade_homem_maior = 0

"""
for pessoa in range(1, 5):
    print("----- {}ª pessoa -----".format(pessoa))
    print("-=" * 15)
    nome = str(input("Digite seu nome {}/{}: ".format(pessoa, 5)).strip().upper())
    sexo = str(input("Digite o seu sexo HOMEM/MULHER: ".format(pessoa, 5)).strip().upper())
    idade = int(input("Digite sua idade: ".format(pessoa, 5)).strip())
    print("-=" * 15)
    soma += idade

    if sexo.upper() == 'HOMEM' and idade > idade_homem_maior:
        idade_homem_maior = idade
        homem_maior = {"nome": nome, "idade": idade}
    if sexo.upper() == 'MULHER' and idade < 20:
        contador_mulher += 1
media = soma / pessoas
print("A média de idade das {} pessoas é de : {}".format(pessoas, media))
print("O homem mais velho é o {} com {} anos".format(homem_maior['nome'], homem_maior['idade']))
print("Existem {} mulheres menores do que 20 anos".format(contador_mulher))
"""

somaidade = 0
mediaidade = 0
maioridadehomem = 0
nomevelho = ''
totmulher20 = 0

for p in range(1, 5):
    print('----- {} ª PESSOA -----'.format(p))
    nome = str(input("Nome: ")).strip()
    idade = int(input("Idade: "))
    sexo = str(input("Sexo [M/F]: ")).strip()
    somaidade += idade
    if p == 1 and sexo in 'Mm':
        maioridadehomem = idade
        nomevelho = nome
    if sexo in 'Mm' and idade > maioridadehomem:
        maioridadehomem = idade
        nomevelho = nome
    if sexo in 'Ff' and idade < 20:
        totmulher20 += 1
mediaidade = somaidade / 4
print("A média de idade do grupo é de {} anos".format(mediaidade))
print("O homem mais velho tem {} anos e se chama {}.".format(maioridadehomem, nomevelho))
print("Ao todo são {} mulheres com menos de 20 anos".format(totmulher20))