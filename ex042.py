#Refaça o ex035 dos triângulos, acrescentando o recurso de mostrar que tipo de triângulo
#será formado:
'''-Equilatero : Todos lados iguais
----isósceles : dois lados iguais
----Escaleno : Todos os lados diferentes'''

r1 = float(input('Primeiro segmento: '))
r2 = float(input('Segundo segmento: '))
r3 = float(input('Terceiro segmento: '))
if r1 < r2 + r3 and r2 < r1 + r3 and r3 < r2 + r1:
    print('Esses segmentos FORMAM um triângulo ', end='')
    if r1 == r2 == r3:
        print('EQUILATERO 🔺')
    elif r1 != r2 != r3 != r1:
        print('ESCALENO 🔺')
    else:
        print('ISOSCELES 🔺')
else:
    print('Esses segmentos NÃO FORMAM triângulo')










