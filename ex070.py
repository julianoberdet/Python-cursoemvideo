soma = mais = mais_barato = 0
while True:
    nome = str(input('Nome do produto: ')).strip()
    preco = float(input('Preço do produto:R$ '))
    usuario = str(input('Quer continuar:[S/N] ')).upper().strip()[0]
    soma += preco
    if preco > 1000:
        mais += 1
    if usuario == 'N':
        break
print(f'O valor total dos produtos foi R${soma}')
print(f'Temos {mais} produtos com valor acima de R$1000,00')
print(f'O produto mais barato é o {mais_barato}')