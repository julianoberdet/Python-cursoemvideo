'''for c in range(1, 10):
    print(c)
print('fim')'''

#Fazer de 1 a 9 com while
'''c = 1
while c < 10:
    print(c)
    c += 1
print('fim') '''

#Vai ler 4 números só:
'''for c in range(1,5):
    n = int(input('Digite um número: '))
print('fim')'''

#Enquanto o número for diferente de 0, ele continua lendo:
'''n = 1
while n != 0:
    n = int(input('Digite um número: '))
print('fim')'''
#ou seja, no momento que digitar 0, acaba o programa.

#O programa vai perguntar se quer continuar com S.
'''r = 'S'
while r == 'S':
    n = int(input('Digite um valor: '))
    r = str(input('Quer continuar[S/N]? ')).upper()
print('FIM')'''

#Para ver quantos números pares e impares foram digitados:
'''n = 1
par = impar = 0
while n != 0:
    n = int(input('Digite um valor: '))
    if n != 0 :
        if n % 2 == 0:
            par += 1
        else:
            impar += 1
print(f'Foram digitados {par} pares e {impar} impares ')'''

