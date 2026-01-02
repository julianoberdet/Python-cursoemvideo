matriz = [[0,0,0],[0,0,0],[0,0,0]]
#seguinte: PARA CADA LINHA[l] HAVERÁ 3 COLUNAS[c]. Como é 3x3 o for l(0,3) e (0,3)
for l in range(0,3):
    for c in range(0,3):
        matriz[l][c] = int(input(f'Digite um valor para [{l},{c}]: '))
print('-='*25)
for l in range(0,3):
    for c in range(0,3):
        print(f'[{matriz[l][c]:^5}]',end='')
    print()
