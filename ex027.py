#Faça um programa que leia o nome completo de uma pessoa, mostrando em seguida o primeiro
#e o ultimo nome separadamente

nome = input('Digite seu nome completo: ').strip()
primeironome = nome.split()
segundonome = nome.split()
ultimonome = nome.split()
print(f'Primeiro={primeironome[0]}')
print(f'Segundo={segundonome[1]}')
print(f'ultimo={ultimonome[2]}')