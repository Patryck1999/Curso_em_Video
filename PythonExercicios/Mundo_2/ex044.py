"""
Elabore um programa que calcule o valor a ser pago por um produto, considerando o seu preço normal e
condição de pagamento:
- À vist dinheiro/cheque: 10% de desconto
- À vista no cartão: 5% de desconto
- em até 2x no cartão: preço normal
- 3x ou mais no cartão: 20% de juros
"""
print('{:=^40}'.format(' Lojas Patryck '))
produto = float(input("Digite o valor do produto R$"))
print("1 - À vista dinheiro/cheque: 10% de desconto")
print("2 - À vista no cartão: 5% de desconto")
print("3 - em até 2x no cartão: preço normal")
print("4 - 3x ou mais no cartão: 20% de juros")
opcao = int(input("Digite uma forma de pagamento: "))
if opcao == 1:
    produto_com_desconto = produto - (produto * 10 / 100)
    print("Você escolheu a 1 opção, portanto o valor ficou {:.2f}".format(produto_com_desconto))
elif opcao == 2:
    produto_com_desconto = produto - (produto * 5 / 100)
    print("Você escolheu a 2 opção, portanto o valor ficou {:.2f}".format(produto_com_desconto))
elif opcao == 3:
    mensal = produto / 2
    print("Sua compra será parcelada em até 2x de R${:.2f} SEM JUROS".format(mensal))
    print("Sua compra de R${:.2f} vai custar o mesmo valor do que se fosse à vista".format(produto))
elif opcao == 4:
    parcela = int(input("Quantas parcelas? "))
    if parcela < 3:
        print("Número de parcelas não confere com a opção escolhida, digite um número de 3 parcelas ou mais.")
    else:
        juros = (produto + (produto * 20 / 100))
        mensal = juros / parcela
        print("Sua compra será parcelada em até {}x de R${:.2f} COM JUROS".format(parcela, mensal))
        print("Sua compra de R${:.2f} vai custar R${:.2f} no final".format(produto, juros))
else:
    print("A opção digitada não existe!")
