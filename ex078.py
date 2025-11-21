listanum = []
mai = men = 0
for c in range(0,5):
    listanum.append(int(input(f'Digite um valor para a posição {c+1}: ')))

#Para ver o maior e menor
    if c == 0:
        mai = men = listanum[c]
    else:
        if listanum[c] > mai:
            mai = listanum[c]
        if listanum[c] < men:
            men = listanum[c]

#Ver a lista completa
print('=-'*30)
print(f'Você digitou os números {listanum}')

#Para ver as posições dos maiores
print(f'O maior valor digitado foi: \033[34m{mai}\033[m nas posições', end='')
for i,v in enumerate(listanum):
    if v == mai:
        print(f' {i+1}...', end='')
print()

#Para ver as posições dos menores
print(f'O menor valor digitado foi: \033[32m{men}\033[m nas posições', end='')
for i, v in enumerate(listanum):
    if v == men:
        print(f' {i+1}...', end='')
print()








#Maneira que eu fiz
'''num = list()
maior = menor = pos_maior = pos_menor = 0
for cont in range(0,5):
    num.append(int(input(f'Digite o valor da posição {cont}: ')))
print('-='*30)
print(f'Você digitou os valores: {num}')
for i,c in enumerate(num):
    if i == 0:
        maior = menor = c
        pos_maior = pos_menor = i
    else:
        if c > maior:
            maior = c
            pos_maior = i
        if c < menor:
            menor = c
            pos_menor = i
print(f'O maior número é {maior} e está na posição {pos_maior}')
print(f'O menor número é {menor} e está na posição {pos_menor}')'''