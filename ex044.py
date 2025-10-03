#Elabore um programa que calcule o valor a ser pago por um produto, considerando o seu preço normal
#e condição de pagamento:
'''À Vista: dinheiro/cheque: 10% de desconto
---À Vista no cartão: 5% de desconto
---Em até 2x no cartão : preço normal
---30x ou mais no cartão : 20% de juros'''

valor = float(input('Qual o valor do produto? '))
pagamento = str(input('Qual a forma de pagamento? ')).strip().lower()
cartao = valor - (valor * 0.05)
parcela = valor + (valor * 0.20)
if pagamento in ['dinheiro', 'pix']:
    dinheiro = valor - (valor * 0.10)
    print(f'O valor no dinheiro ou no pix ficará R${dinheiro:.2f}')
elif pagamento in ['a vista no cartao']:
    dinheiro = valor - (valor * 0.05)
    print(f'O valor a vista no cartão ficará {dinheiro:2f}')
elif pagamento in ['2x no cartao']:
    print(f'O valor em 2x no cartão ficará R${valor:.2f}')
elif pagamento in ['30x no cartao']:
    dinheiro = valor + (valor * 0.20)
    print(f'Parceado em 30x ficará a prazo o vaor de R${dinheiro:.2f}')

