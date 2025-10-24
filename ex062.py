primeiro = int(input('Primeiro termo: '))
razao = int(input('Razão da PA: '))
termo = primeiro
cont = 1
mais = 10
total = 0
while mais != 0:
    total += mais
    while cont <= total:
        print(f'{termo}', end= ' -> ')
        cont += 1
        termo += razao
    print('PAUSA')
    mais = int(input('Quantos termos a mais você quer? '))
print(f'Progressão finalizada com {total} termos mostrados!')



