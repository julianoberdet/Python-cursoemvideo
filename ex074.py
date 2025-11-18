from random import randint
num = (randint(0,10) , randint(0,10) , randint(0,10) , randint(0,10) ,
randint(0,10))
print(f'Os valores sorteados foram: ',end='')
for n in num:
    print(f'{n} ',end=' ')
print(f'\nO menor valor foi {min(num)}, e o maior foi {max(num)}')










#Jeito que eu fiz
'''from random import randint
numero1 = randint(0, 100)
numero2 = randint(0, 100)
numero3 = randint(0, 100)
numero4 = randint(0, 100)
numero5 = randint(0, 100)
aleatorio = (numero1, numero2, numero3, numero4, numero5)
print(f'Os valores sorteados foram: {aleatorio}')
maior = max(aleatorio)
menor = min(aleatorio)
print(f'O maior número sorteado foi {maior} e menor foi {menor}')'''
