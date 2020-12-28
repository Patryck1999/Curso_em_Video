"""
Desenvolva um programa que leia seis números inteiros e mostre a soma apenas daqueles que forem pares. Se o valor
digitado for impar, desconsidere-o.
"""
final = 6
soma = 0
cont = 0
for valor in range(1, final + 1):
    numero = int(input("Digite o {}/{} para que possa ser somado caso seja par: ".format(valor, final)))
    if numero % 2 == 0:
        soma += numero
        cont += 1
print("A soma dos {} valores pares é de {}".format(cont, soma))
