"""
Crie um programa que leia o nome de uma cidade e diga se ela começa ou não com o nome "SANTO"
"""
"""cidade = str(input("Digite o nome de uma cidade: \n").upper().strip())

print("A cidade {} começa com SANTO, True ou False? {}".format(cidade, "SANTO" == cidade.split()[0]))"""

cid = str(input("Digite o nome de uma cidade: \n").upper().strip())
print(cid[:5] == "SANTO")
