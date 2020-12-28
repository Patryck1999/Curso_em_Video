"""
Faça um programa que leia o nome completo de uma pessoa, mostrando em seguida o primeiro e o ultimo nome
separadamente.

Ex: Ana Maria de Souza
primeiro = Ana
Ultimo = Souza
"""
"""
nome_completo = str(input("Digite o nome completo: \n")).strip()
print("Primeiro nome {} \nUltimo nome {}".format(nome_completo.split()[0], nome_completo.split()[-1]))
"""
nome_completo = str(input("Digite o nome completo: \n")).strip()
print("Primeiro nome {}".format(nome_completo.split()[0]))
print("Ultimo nome {}".format(nome_completo.split()[len(nome_completo.split()) - 1]))

