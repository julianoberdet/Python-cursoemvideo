n = float(input('Quantos dias alugados? '))
m = int(input('Quantos km rodados? '))
valor = (n * 60) + (m * 0.15)
print(f'o preço do carro ficará R${valor:.2f}!')
