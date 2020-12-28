"""
Crie um programa que leia o nome e o preço de vários produtos. O programa deverá perguntar se o usuário vai continuar.
No final, mostre:
A) Qual é o total gasto na compra.
B) Quantos produtos custam mais que R$1000.
C) Qual é o nome do produto mais barato.
"""
print("-" * 40)
print(f"{'LOJA SUPER BARATÃO':^40}")
print("-" * 40)
total = 0
produto_maior_1000 = 0
contador = 0
preco_barato = 0
produto_barato = ''
while True:
    produto = str(input("Nome do produto: "))
    preco = float(input("Preço R$"))
    total += preco
    contador += 1
    resposta = " "
    while resposta not in "SsNn":
        resposta = str(input("Quer continuar? [S/N] ")).upper().strip()
    if preco > 1000:
        produto_maior_1000 += 1
    if contador == 1 or preco < preco_barato:
        preco_barato = preco
        produto_barato = produto
    if resposta == 'N':
        break
print(f"{'FIM DO PROGRAMA':-^40}")
print(f"O total da compra foi R${total:.2f}")
print(f"Temos {produto_maior_1000} produtos custando mais de R$1000.00")
print(f"O produto mais barato foi {produto_barato} que custa R${preco_barato:.2f}")
