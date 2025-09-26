#Escreva um programa que leia a velocidade de um carro. Se ele ultrapassar 80km\h, mostre uma
#mensagem dizendo que ele foi multado. a multa vai custar R$7,00 por cada km acima do limite

velocidade = float(input('Qual foi a velocidade que passou no radar? '))
if velocidade > 80:
    print(f'VOCÊ FOI MULTADO! Pois excedeu o limite permitido de 80km/h')
    m = (velocidade - 80) * 7
    print(f'Você pagara uma multa de R${m:.2f}')
print('Tenha um bom dia! Dirija com segurança.')
