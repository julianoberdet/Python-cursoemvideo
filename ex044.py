#Elabore um programa que calcule o valor a ser pago por um produto, considerando o seu preço normal
#e condição de pagamento:
'''À Vista: dinheiro/cheque: 10% de desconto
---À Vista no cartão: 5% de desconto
---Em até 2x no cartão : preço normal
---30x ou mais no cartão : 20% de juros'''

print(f"{' LOJAS BERDET ':=^40}")
valor = float(input('Qual o valor do produto? '))
print('''FORMAS DE PAGAMENTO:
[ 1 ] - Dinheiro/Pix (10% de desconto)
[ 2 ] - Cartão Débito (5% de desconto)
[ 3 ] - 2x no cartão (sem desconto)
[ 4 ] - 3x ou mais no cartão (20% de juros)''')
pagamento = int(input('Qual a forma de pagamento? '))
if pagamento == 1:
    total = valor * 0.90
elif pagamento == 2:
    total = valor * 0.95
elif pagamento == 3:
    total = valor
    parcela = valor / 2
    print(f'Sua compra será parcelada em 2x de {parcela:.2f}')
elif pagamento == 4:
    pcls = int(input('Quantas vezes quer fazer? '))
    total = valor * 1.20
    parcela = total / pcls
    if pcls >= 3:
        print(f'Parcelado em {pcls}x a parcela será R${parcela:.2f}.')
    elif pcls < 3:
        print('Opção invalida, tente novamente')
else:
    total = valor
    print('\033[31mOPÇÃO INVALIDA\033[m, tente novamente!')
print(f'Sua compra de {valor:.2f} ficará R${total:.2f} no final.')
