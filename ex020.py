#O mesmo professor do desafio anterior quer sortear a orden de apresentação de
#trabalho dos aunos. Faça um programa que leia o nome dos quatro alunos e mostre a
#ordem sorteada:

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
