#Faça um programa que leia o ângulo qualquer e mostre na tela o valor do seno,
#cosseno e tangente desse ângulo:

#import math
#angulo = float(input('Digite um ângulo qualquer: '))
#seno = math.sin(math.radians(angulo))
#cosseno = math.cos(math.radians(angulo))
#tangente = math.tan(math.radians(angulo))
#print(f'O Seno de {angulo} é {seno:.2f}\nO Cosseno de {angulo} é {cosseno:.2f}\nA tangente de {angulo} é {tangente:.2f}')
#JEITO QUE EU FIZ

from math import radians, sin, cos , tan
angulo = float(input('Digite um ângulo qualquer: '))
seno = sin(radians(angulo))
print(f'O SENO de {angulo} é {seno:.2f}')
cosseno = cos(radians(angulo))
print(f'O COSSENO de {angulo} é {cosseno:.2f}')
tangente = tan(radians(angulo))
print(f'A TANGENTE de {angulo} é {tangente:.2f}')