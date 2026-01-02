matriz = [[0,0,0],[0,0,0],[0,0,0]]
soma = maior = menor = somcol = 0
for l in range(0,3):
    for c in range(0,3):
        matriz[l][c] = int(input(f'Digite um valor para [{l},{c}]: '))
print('-='*25)
for l in range(0,3):
    for c in range(0,3):
        print(f'[{matriz[l][c]:^5}]',end='')
#Somar os valores pares da matriz
        if matriz[l][c] % 2 == 0:
            soma += matriz[l][c]
    print()
print('-='*25)
print(f'A soma entre todos os números pares da matriz é {soma}')

#Somar os valores da terceira coluna
for l in range(0,3):
    somcol += matriz[l][2]  #a coluna ja está fixada o que vai variar é a linha
print(f'A soma dos valores da terceira coluna é {somcol}')

#Saber o maior valor da segunda linha
for c in range(0,3):
    if c == 0 or matriz[1][c] > maior:
        maior = matriz[1][c]
print(f'O maior número da segunda linha é {maior}')

#Saber o menor valor da primeira linha
for c in range(0,3):
    if c == 0 or matriz[0][c] < menor:
        menor = matriz[0][c]
print(f'O menor valor da primeira linha é {menor}')