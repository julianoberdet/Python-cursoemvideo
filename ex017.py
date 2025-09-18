#Faça um programa que leia o comprimento do cateto oposto do cateto adjacente de
#um triângulo retangulo, calcule e mostre o comprimento da hipotenusa:


#co = float(input('Digite o cateto oposto: '))
#ca = float(input('Digite o cateto adjacente: '))
#hi = (ca ** 2 + co ** 2) ** (1/2)
#print(f'sendo assim a hipotenusa é {hi:.2f}')
#Maneira matemática sem importar a biblioteca

from math import hypot
co = float(input('Digite o cateto oposto: '))
ca = float(input('Digite o cateto adjacente: '))
hi = hypot(co,ca)
print(f'A hipotenusa será {hi:.2f}!')