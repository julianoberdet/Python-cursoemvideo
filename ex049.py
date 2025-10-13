m = 0
n = int(input('Digite um número para saber sua tabuada: '))
for c in range(0 , 10+1, 1):
    m = n * c
    print(f'{n} x {c} = {m}')
