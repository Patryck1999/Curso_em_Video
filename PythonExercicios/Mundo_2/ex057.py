"""
Faça um programa que leia o sexo de uma pessoa, mas só aceite os valores "M" ou "F". Caso esteja errado peça a digitação
novamente até ter um valor COrreto.
"""

"""
sexo = str(input("Digite o seu sexo M/F: ")).upper().strip()[0]
while sexo != "M" and sexo != "F":
    if sexo != "M" and sexo != "F":
        sexo = str(input("Dados inválidos por favor informe seu sexo: ")).upper()
"""
sexo = str(input("Informe seu sexo: [M/F] ")).strip().upper()[0]
while sexo not in 'MmFf':
    sexo = str(input("Dados inválidos. Por favor, informe seu sexo: ")).strip().upper()[0]
print("Sexo {} registrado com sucesso".format(sexo))
