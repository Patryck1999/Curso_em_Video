"""
Faça um programa que leia algo pelo teclado e mostre na tela o seu tipo primitivo
e todas as informações possiveis sobre ele.
"""
n = input("Digite um valor: ")
print("O tipo primitivo desse valor é", type(n))
print("Esse valor tem somente espaços", n.isspace())
print("Esse valor pode ser convertido em um número: ", n.isnumeric())
print("Esse valor é de um alfabeto: ", n.isalpha())
print("Esse valor é um alfabeto com números: ", n.isalnum())
print("Esse valor tem todas as letras maiúsculas: ", n.isupper())
print("Esse valor todos as letras são minúsculas: ", n.islower())
print("Esse valor tem a inicial maiúsculas e o restante minusculo:", n.istitle())
print("Esse valor esta na tabela asc: ", n.isascii())
print("Esse valor pode ser convertido para um número decimal: ", n.isdecimal())
print("Esse valor é um digito inteiro positivo: ", n.isdigit())
print("Esse valor pode ser um identificador: ", n.isidentifier())
print("Esse valor pode ser printado na tela: ", n.isprintable())


