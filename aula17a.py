'''num = (2,5,9,1)
num[2]= 9
print(num)''' #Em tupla não pode, por que tupla é imutável

#EXEMPLOS
'''#Mas em lista pode, por que é mutavel
num = [2,5,9,1]
num [2] = 3 #Para trocar o numero 9 por 3
num.append(7) #para adicionar um número no fim
#num.sort() #Em ordem
num.sort(reverse=True) #Em ordem reversa
num.insert(2, 2) #Pra inserir na posição 2 o número 0

#PARA DELETAR ELEMENTOS
#num.pop() #para eliminar o ultimo elemento
#num.pop(2) #Para eliminar o elemento da posição 2

#SE QUISER APAGAR ALGUM NPUMERO QUE NÃO TENHA NA LISTA VAI DAR ERRO, ENTAO TEM QUE USAR O LAÇO IF/ELSE:
if 4 in num:
    num.remove(4)
else:
    print('Não achei o número 4')

print(num)
print(f'Essa lista tem {len(num)} elementos') #para mostrar quantos elementos tem'''

#OUTRO EXEMPLO
'''valores = list()
for cont in range(0,5):
    valores.append(int(input('Digite um valor: ')))
#valores.append(5)
#valores.append(9)
#valores.append(4)
#for v in valores:
#    print(f'{v}...',end='')   5...9...4
for c, v in enumerate(valores):
    print(f'Na posição {c} encontrei o valor {v}')
print('Cheguei ao final da lista')'''

#OUTRO EXEMPLO

#Ligação
a = [2,3,4,7]
b = a
b[2] = 8
print(f'Lista A = {a}')
print(f'Lista B = {b}')

#Cópia
a = [2,3,4,7]
b = a[:]
b[2] = 8
print(f'Lista A = {a}')
print(f'Lista B = {b}')