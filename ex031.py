#Desenvolva um programa que pergunte a distancia de uma viagem em Km. Calcule o preço da passagem,
#cobrando R$0,50 por Km para viagens de até 200km e R$0,45 para viagens mais longas.

d = float(input('Qual a distância da viagem? '))
print(f'Você está prestes a começar uma viagem de {d}km')
if d <= 200:
    preço = d * 0.5
else:
    preço = d * 0.45
print(f'Sua viagem vai custar R${preço:.2f}')