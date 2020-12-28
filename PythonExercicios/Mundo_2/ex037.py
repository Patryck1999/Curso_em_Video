"""
Escreva um programa que leia um numero inteiro qualquer e peça para o usuário escolher qual será a base de conversão:

- 1 para binario
- 2 para octal
- 3 para hexadecimal


lista = []
numero = int(input("Digite um número: "))
print("Digite 1 - para converter para binário")
print("Digite 2 - para converter para octal")
print("Digite 3 - para converter para hexadecimal")
opcao = int(input("Digite uma opção de 1 a 3 para converter o número digitado: "))
resultado = ''
while numero > 0:
    if opcao <= 0 or opcao > 3:
        print("Opção Invalida!")
        break
    elif opcao == 1:
        resto = numero % 2
        inteiro = numero // 2
        lista.append(resto)
        numero = inteiro
        binario = str(lista).strip('[]').replace(',', '')
        resultado = ''.join(binario.split()[::-1])

    elif opcao == 2:
        resto = numero % 8
        inteiro = numero // 8
        lista.append(resto)
        numero = inteiro
        octal = str(lista).strip('[]').replace(',', '')
        resultado = ''.join(octal.split()[::-1])

    elif opcao == 3:
        resto = numero % 16
        inteiro = numero // 16
        numero = inteiro
        lista.append(resto)
        hexadecimal = str(lista).strip("[]").replace(",", "")
        resultado = "".join(hexadecimal.split()[::-1]).replace("10", "A").replace("11", "B").replace("12", "C").replace("13", "D").replace("14", "E").replace("15", "F")
print("O valor é: {}".format(resultado))
"""

num = int(input("Digite um número inteiro: "))
print("""Escolha uma das bases para conversão:
[ 1 ] converter para BINÁRIO
[ 2 ] converter para OCTAL
[ 3 ] converter para HEXADECIMAL""")
opcao = int(input("Sua opção: "))

if opcao == 1:
    print("{} convertido para BINÁRIO é igual a {}".format(num, bin(num)[2:]))
elif opcao == 2:
    print("{} convertido para OCTAL é igual a {}".format(num, oct(num)[2:]))
elif opcao == 3:
    print('{} convertido para HEXADECIMAL é igual a {}'.format(num, hex(num)[2:]))
else:
    print("Opção inválida. Tente novamente")
