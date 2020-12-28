"""
Crie um programa que leia dois valores e mostre um menu na tela:
[1] somar
[2] multiplicar
[3] maior
[4] novos números
[5] sair do programa
OBS: Seu programa deverá realizar a operação solicitada em cada caso.
"""
opcao = 0
numero_1 = float(input("Digite o primeiro valor: "))
numero_2 = float(input("Digite o segundo valor: "))
while opcao != 5:
    print("""    [1] somar
    [2] multiplicar
    [3] maior
    [4] novos números
    [5] sair do programa""")
    opcao = int(input("Digite a opção desejada: "))
    if opcao == 1:
        somar = numero_1 + numero_2
        print("A soma entre {} e {} é de: {}".format(numero_1, numero_2, somar))
    elif opcao == 2:
        multiplicar = numero_1 * numero_2
        print("A soma entre {} e {} é de: {}".format(numero_1, numero_2, multiplicar))
    elif opcao == 3:
        if numero_1 > numero_2:
            print("O número {} é maior do que o número {}".format(numero_1, numero_2))
        elif numero_2 > numero_1:
            print("O número {} é maior do que o número {}".format(numero_2, numero_1))
        else:
            print("Os dois números são iguais")
    elif opcao == 4:
        print("Digite os números novamente")
        numero_1 = float(input("Digite o primeiro valor: "))
        numero_2 = float(input("Digite o segundo valor: "))
    elif opcao == 5:
        print("Finalizando...")
    elif opcao < 0 or opcao > 5:
        print("Opção inválida!")
print("Fim do programa!")
