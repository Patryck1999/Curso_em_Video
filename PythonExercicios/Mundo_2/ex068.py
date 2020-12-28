"""
Faça um programa que jogue par ou impar com o computador. O jogo só será interrompido quando o jogador PERDER, mostrando
o total de vitórias consecutivas que ele conquistou no final do jogo.
"""
"""
from random import randint
print("=-" * 16)
print("VAMOS JOGAR PAR OU ÍMPAR")
print("=-" * 16)
vitorias = 0
derrotas = 0
soma = 0
while derrotas == 0:
    computador = randint(0, 10)
    numero = int(input("Digite um valor: "))
    palpite = str(input("Par ou Ímpar? ")).strip().upper()
    soma = computador + numero
    if soma % 2 == 0:
        jogo = "PAR"
    else:
        jogo = "IMPAR"
    print("-" * 58)
    print(f"Você jogou {numero} e o computador jogou {computador}. Total de {soma} Deu {jogo}")
    print("-" * 58)
    if palpite == "PAR" and soma % 2 == 0:
        print("Você VENCEU!")
        vitorias += 1
    elif palpite == "IMPAR" and soma % 2 == 1:
        print("Você VENCEU!")
        vitorias += 1
    else:
        print("Você PERDEU!")
        derrotas += 1
        break
print("=-" * 16)
print(f"Game OVER! Você venceu {vitorias} vezes")
"""
from random import randint
v = 0
while True:
    jogador = int(input("Diga um valor: "))
    computador = randint(0, 10)
    total = jogador + computador
    tipo = ' '
    while tipo not in "PI":
        tipo = str(input("Par ou Ímpar? [P/I] ")).strip().upper()[0]
    print(f"Você jogou {jogador} e o computador {computador}. Total de {total} ", end="")
    print("DEU PAR" if total % 2 == 0 else "DEU ÍMPAR")
    if tipo == "P":
        if total % 2 == 0:
            print("Você VENCEU!")
            v += 1
        else:
            print("Você PERDEU!")
            break
    elif tipo == "I":
        if total % 2 == 1:
            print("Você VENCEU!")
            v += 1
        else:
            print("Você PERDEU!")
            break
    print("Vamos jogar novamente...")
print(f"GAME OVER! Você venceu {v} vezes")
