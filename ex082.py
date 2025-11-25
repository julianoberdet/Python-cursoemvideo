num = []
par = []
impar = []
while True:
    num.append(int(input('Digite um valor: ')))
    resp = ' '
    while resp not in 'SN':
        resp = str(input('Quer continuar?[S/N] ')).strip().upper()[0]
    if resp == 'N':
        break
for i, v in enumerate(num):
    if v % 2 == 0:
        par.append(v)
    elif v % 2 == 1:
        impar.append(v)
print(f'A lista completa ficou assim: {num}')
print(f'Os números pares são: {par}')
print(f'Os números impares são: {impar}')









#Jeito que eu fiz
'''num = list()
par = list()
impar = list()
while True:
    numero = int(input('Digite um valor: '))
    num.append(numero)
    if numero % 2 == 0:
        par.append(numero)
    if numero % 2 == 1:
        impar.append(numero)
    resp = ' '
    while resp not in 'SN':
        resp = str(input('Quer continuar?[S/N] ')).strip().upper()[0]
    if resp == 'N':
        break
print(f'A lista completa ficou assim: {num}')
print(f'Os número pares são: {par}')
print(f'E os impares são: {impar}')'''
