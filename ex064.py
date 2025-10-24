tot = soma = 0
n = int(input('Digite um número:[Digite 999 para parar] '))
while n != 999:
    tot += 1
    soma += n
    n = int(input('Digite um número:[Digite 999 para parar] '))
print(f'Você digitou {tot} número e a soma deles é {soma}')


