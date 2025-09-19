#Crie um programa que leia o nome de uma cidade e diga se ela começa com o nome "Santo"

cid = str(input('Digite o nome de uma cidade: ')).strip().upper()
print(cid[:5] in 'SANTO')