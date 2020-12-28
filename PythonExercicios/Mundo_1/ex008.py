"""
Escreva um programa que leia um valor em metros e o exiba convertido em centimetros e milímetros.

km(Quilómetro) -> Hm(Hectómetro) -> Dam(Decâmetro) -> M(Metro ->) Dm(Decímetro) -> Cm(Centímetro)-> mm(Milímetro)
    1                  0                0                  0            0                 0             0

"""
valor = float(input("Digite o valor em metros para que possa ser convertido: "))
km = valor / 1000
hm = valor / 100
dam = valor / 10
dm = valor * 10
cm = valor * 100
mm = valor * 1000

print("A medida de {:.0f} metros \ncorresponde {:.0f} quilómetros \n{:.0f} hectómetros".format(valor, km, hm, ))
print("{:.0f} Decâmetros \n {:.0f} decímetros \n {:.0f} centímetros \n {:.0f} milímetros".format(dam, dm, cm, mm))
