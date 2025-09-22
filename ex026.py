#Faça um programa que leia uma frase pelo teclado e mostre: Quantas vezes aparece a
#letra A, em que posição ela aparece a primeira vez, em que posição ela aparece a ultima vez

frase = str(input('Digite uma Frase: ')).strip().upper()
print(f'Essa frase contem {frase.count('A')} letras "A"')
print(f'A letra A aparece a primeira vez no caractere {frase.find('A')+1}')
print(f'E a última vez que a letra A aparece é no caractere {frase.rfind('A')+1}')

