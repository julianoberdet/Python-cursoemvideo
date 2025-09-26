#Desenvolva um programa que pergunte a distancia de uma viagem em Km. Calcule o preço da passagem,
#cobrando R$0,50 por Km para viagens de até 200km e R$0,45 para viagens mais longas.

d = float(input('Qual a distância da viagem? '))
p = d * 0.50
if d <= 200:
    print(f'Sua viagem vai custar {p:.2f}')
else:
    print(f'Sua viagem vai custar {d*0.45:.2f}')