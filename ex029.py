#Escreva um programa que leia a velocidade de um carro. Se ele ultrapassar 80km\h, mostre uma
#mensagem dizendo que ele foi multado. a multa vai custar R$7,00 por cada km acima do limite

v = float(input('Qual foi a velocidade que passou no radar? '))
m = (v-80)*7
if v >= 80:
    print(f'Você foi multado, e pagará a multa de R${m:.2f}')
else:
    print('Siga em frente!')
