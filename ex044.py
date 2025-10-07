#Elabore um programa que calcule o valor a ser pago por um produto, considerando o seu preço normal
#e condição de pagamento:
'''À Vista: dinheiro/cheque: 10% de desconto
---À Vista no cartão: 5% de desconto
---Em até 2x no cartão : preço normal
---30x ou mais no cartão : 20% de juros'''

valor = float(input('Qual o valor do produto? '))
print('\nFormas de pagamento:')
print('1 - Dinheiro/Pix (10% de desconto)')
print('2 - Cartão Débito (5% de desconto)')
print('3 - 2x no cartão (sem desconto)')
print('4 - 30x no cartão (20% de juros)')
pagamento = input('Qual a forma de pagamento? ')
if pagamento in ['1']:
    dinheiro = valor * 0.90
    print(f'O valor no dinheiro ou no pix ficará R${dinheiro:.2f}')
elif pagamento in ['2']:
    total = valor * 0.95
    print(f'O valor ficará R${total:.2f}')
elif pagamento in ['3']:
    parcela = valor / 2
    print(f'O valor em 2x no cartão é R${parcela:.2f} e ficará R${valor:.2f}')
elif pagamento in ['4']:
    total = valor * 1.20
    parcela = valor / 30
    print(f'Parcelado em 30x o valor da parcela será R${parcela:.2f} e o valor total é R${total:.2f}')

