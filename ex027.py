#Faça um programa que leia o nome completo de uma pessoa, mostrando em seguida o primeiro
#e o ultimo nome separadamente

n = input('Digite seu nome completo: ').strip()
print(f'Muito prazer em te conhecer, {n}!')
nome = n.split()
print(f'Seu primeiro nome é {nome[0]}')
print(f'Seu segundo nome é {nome[1]}')
print(f'E seu último nome é {nome[len(nome)-1]}')