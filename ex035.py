#Desenvolva um programa que leia o comprimento de três retas e diga ao usuário se elas podem
#ou não formar um triângulo.

r1 = float(input('Digite o comprimento dessa reta: '))
r2 = float(input('Digite o comprimento dessa reta: '))
r3 = float(input('Digite o comprimento dessa reta: '))
if r1 + r2 > r3 and r2 +r1 > r3 and r3 + r2 > r1:
    print('Com esses comprimentos de reta podemos montar um triângulo')
else:
    print('Infelizmente não vai dar pra montar o triângulo')