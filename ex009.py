real = float(input('Quanto dinheiro tens na carteira?  R$'))
dolar = 5.40
euro = 6.30
d = real/dolar
e = real/euro
print(f'Com esse dinheiro que tenho, sabendo que valor do dolar está {dolar:.2f}US$ e do euro {euro:.2f}£, posso comprar {d:.2f}US$ e {e:.2f}£!')
