from random import shuffle
a = input('Primeiro aluno: ')
b = input('Segundo aluno: ')
c = input('Terceiro aluno: ')
d = input('Quarto aluno: ')
e = input('Quinto aluno: ')
lista = [a,b,c,d,e]
shuffle(lista)
print('O sorteio ficou assim para a apresentação: ')
print(lista)
