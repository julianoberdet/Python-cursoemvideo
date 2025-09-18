#Um professor quer sortear um dos seus quatro alunos para apagar o quadro. Faça
#um programa que ajude ele, lendo o nome deles e escrevendo o nome do escolhido:

from random import choice
a = input('Primeiro aluno: ')
b = input('Segundo aluno: ')
c = input('Terceiro aluno: ')
d = input('Quarto aluno: ')
e = input('Quinto aluno: ')
lista = [a,b,c,d,e]
sorteio = choice(lista)
print(f'O aluno escolhido foi {sorteio}!')