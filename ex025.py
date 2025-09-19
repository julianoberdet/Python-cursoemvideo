#Crie um programa que leia o nome de uma pessoa e diga se ela tem Silva no nome

nome = input('Digite seu nome completo: ').strip().upper()
print(f'Seu nome tem Silva? {'SILVA'in nome}')
#print(f'Seu nome tem Silva? {'silva' in nome.lower()}')