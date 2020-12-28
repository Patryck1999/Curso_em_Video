"""
Desenvolva um programa que leia o primeiro termo e a razão de uma PA. No final mostre os 10 primeiros termos
dessa progressão.
"""
"""
a1 = int(input("Digite o primeiro termo: "))
a2 = int(input("Digite a razão de uma PA: "))
pa = a1
if a1 > 0 or a1 == 0:
    for numero in range(1, 10 + 1):
        print(pa, end=" -> ")
        pa += a2
elif a1 < 0:
    for numero in range(1, 10 + 1):
        print(pa)
        pa -= a2
print("Fim")
"""
primeiro = int(input("Digite o primeiro termo: "))
razao = int(input("Digite a razão de uma PA: "))
decimo = primeiro + (10 - 1) * razao
for c in range(primeiro, decimo + razao, razao):
    print("{} ".format(c), end=" -> ")
print("Acabou")
