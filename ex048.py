s = 0
for c in range(1 , 501):
    if c % 2 != 0 and c % 3 == 0:
        s += c
print(f'A soma de todos os impares multiplos de 3 é {s}')
