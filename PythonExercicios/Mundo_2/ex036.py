"""
Escreva um programa para aprovar o empréstimo bancário para a compra de uma casa. O programa vai perguntar
o valor da casa, o salário do comprador e em quantos anos ele vai pagar.
calcule o valor da prestação mensal, sabendo que ela não pode exceder 30 % do salário ou então o empréstimo
será negado.
"""

valor_casa = float(input("Digite o valor da casa: R$"))
salario = float(input("Digite seu salário: R$"))
anos = int(input("Digite até quantos você quer pagar: R$"))
prestacao_mensal = valor_casa / (anos * 12)
condicao = (salario * 30 / 100)
print('O valor do pagamento da casa por mês é de R${:.2f} durante {} anos'.format(prestacao_mensal, anos))
print('O valor limite de 30 % para adquirir o empréstimo é de R${:.2f}'.format(condicao))
if prestacao_mensal <= condicao:
    print("Empréstimo pode ser CONCEDIDO!")
elif prestacao_mensal > condicao:
    print("Empréstimo NEGADO!")
