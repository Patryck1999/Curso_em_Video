"""
Escreva um programa que converta uma temperatura digitada em ºC e converta para ºF
"""
celsius = float(input("Informe a temperatura em Celsius: "))
fahrenheit = ((celsius * 9) / 5) + 32
print("A temperatura de {}ºC corresponde a {}ºF".format(celsius, fahrenheit))
