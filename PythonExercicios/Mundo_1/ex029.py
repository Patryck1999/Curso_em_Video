"""
Escreva um programa que leia a velocidade de um carro.
Se ele ultrapassar 80Km/h, mostre uma mensagem dizendo que ele foi multado.
A multa vai custar R$7,00 por cada Km acima do limite.
"""
velocidade = float(input("Digite a velocidade em que seu carro está andando: "))
limite_velocidade = float(80.00)
if velocidade > limite_velocidade:
    print("Você passou do limite de até {:.2f} Km/h".format(limite_velocidade))
    velocidade_excedida = velocidade - limite_velocidade
    multa = velocidade_excedida * 7.00
    print("A multa por ter excedido {:.2f} Km/h acima do limite foi de R${:.2f}".format(velocidade_excedida, multa))
print("Boa viagem, cuidado na estrada!")
