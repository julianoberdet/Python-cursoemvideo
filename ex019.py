from random import choice
a = input('Primeiro aluno: ')
b = input('Segundo aluno: ')
c = input('Terceiro aluno: ')
d = input('Quarto aluno: ')
e = input('Quinto aluno: ')
lista = [a,b,c,d,e]
sorteio = choice(lista)
print(f'O aluno escolhido foi {sorteio}!')