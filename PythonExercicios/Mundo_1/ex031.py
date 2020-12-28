"""
Desenvolva um programa que pergunte a distância de uma viagem em km. Calcule o preço da passagem, cobrando R$0,50
por Km para viagens de até 200Km e R$0,45 para viagens mais longas.
"""
"""
distancia = float(input("Digite a distância para o seu destino: "))

if distancia <= 200.00:
    passagem = distancia * 0.50
else:
    passagem = distancia * 0.45
print("Seu destino tem {:.2f} Km, o valor total é de R${:.2f}".format(distancia, passagem))
    """

distancia = float(input("Digite a distância para o seu destino: "))
preco = distancia * 0.50 if distancia <= 200.00 else distancia * 0.45
print("Seu destino tem {:.2f} Km, o valor total é de R${:.2f}".format(distancia, preco))
