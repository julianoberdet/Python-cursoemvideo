#Desenvolva um programa que eia seis números inteiros e mostre a soma apenas daqueles que forem pares

cont = 0
soma = 0
for c in range(1 , 7):
    n = int(input(f'Digite o {c}º valor: '))
    if n % 2 == 0:
      soma += n
      cont += 1
print(f'Você informou {cont} números PARES e a soma deles é {soma}')


