"""
Melhore o DESAFIO 061, perguntando para o usuário se ele quer mostrar mais alguns termos. O programa encerra quando ele
disser que quer mostrar 0 termos.
"""
"""
contador = 1
termos = 10
primeiro_termo = int(input("Digite o primeiro termo: "))
razao = int(input("Digite a razão: "))
acumulador = primeiro_termo

while contador <= termos:
    if contador == 1:
        print(primeiro_termo, end="->")
        contador += 1
    else:
        acumulador += razao
        print(acumulador, end="->")
        contador += 1
    if contador > termos:
        termos = int(input("\nDeseja mostrar mais quantos termos, senão digite 0?"))
        if termos == 0:
            print("Fim do programa")
        else:
            contador = 1
            primeiro_termo = int(input("Digite o primeiro termo: "))
            acumulador = primeiro_termo
            razao = int(input("Digite a razão: "))
"""
print("Gerador de PA")
print("-=" * 10)
primeiro = int(input("Digite o primeiro termo: "))
razao = int(input("Digite a razão: "))
termo = primeiro
contador = 1
total = 0
mais = 10
while mais != 0:
    total = total + mais
    while contador <= total:
        print('{} -> '.format(termo), end="")
        termo += razao
        contador += 1
    print("PAUSA")
    mais = int(input("Quantos termos você quer mostrar a mais? "))
print("Progressão finalizada com {} termos mostrados.".format(total))
