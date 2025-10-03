#Refaça o ex035 dos triângulos, acrescentando o recurso de mostrar que tipo de triângulo
#será formado:
'''-Equilatero : Todos lados iguais
----isósceles : dois lados iguais
----Escaleno : Todos os lados diferentes'''

print('-=-' * 20)
print('Analisando os triângulos..')
print('-=-' * 20)
r1 = float(input('Primeiro segmento: '))
r2 = float(input('Segundo segmento: '))
r3 = float(input('Terceiro segmento: '))
if r1 < r2 + r3 and r2 < r1 + r3 and r3 < r2 + r1:
    print('Esses segmentos formam um triângulo.')
    if r1 == r2 == r3:
        print('Esse triângulo é um EQUILATERO 🔺')
    elif r1 == r2 or r1 == r3 or r2 == r3:
        print('E esse triângulo é classificado como ISÓSCELES 🔺')
    else:
        print('Esse triângulo é um ESCALENO 🔺')
else:
    print('Esses segmentos não formam triângulo')










