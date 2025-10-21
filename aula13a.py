'''for c in range (6 , 0 , -1):
    print(c)
print('FIM')'''

'''for c in range (0 , 70+1 , 7):
    print(c)
print('FIM')'''

'''n = int(input('Digite um número: '))
for c in range(0, n+1):
    print(c)'''

'''i = int(input('Inicio: '))
f = int(input('Fim: '))
p = int(input('Passo: '))
for c in range(i , f+1 , p):
    print(c)
print('FIM')'''#Outra maneira de contagem

s = 0
for c in range(0, 4):
    n = int(input('Digite um número: '))
    s = s + n
print(f'O somatório de todos os valores foi {s}')
