print('-' * 50)
print('                  \033[34;1mLOJAS BERDET\033[m')
print('-' * 50)
total = tot1000 = menor = cont = 0
barato = ''
while True:
    produto = str(input('Nome do produto: ')).strip()
    preco = float(input('Preço do produto:R$ '))
    total += preco
    cont += 1
    if preco > 1000:
        tot1000 += 1
    if cont == 1 or preco < menor:
        menor = preco
        barato = produto
    resp = ' '
    while resp not in 'SN':
        resp = str(input('Quer continuar?[S/N] ')).strip().upper()[0]
    print('-' *50)
    if resp == 'N':
        break
print(f'O total gasto na compra será: R${total:.2f}')
print(f'Foram {tot1000} produtos acima de R$1000,00')
print(f'O produto mais barato foi {barato} e custou R${menor:.2f}')