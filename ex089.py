from time import sleep
ficha = []
while True:
    nome = str(input('Nome: '))
    nota1 = float(input('Nota 1: '))
    nota2 = float(input('Nota 2: '))
    media = (nota1 + nota2) / 2
    ficha.append([nome,[nota1,nota2],media])
    resp= ' '
    while resp not in 'SN':
        resp = str(input('Quer continuar?[S/N] ')).strip().upper()[0]
    if resp == 'N':
        break
print('-=' * 30)
print(f'{"No":<4}{"Nome":<10}{"Média":>8}')
for i, a in enumerate(ficha):
    print(f'{i:<4}{a[0]:<10}{a[2]:>8.1f}')
while True:
    print('-=' * 30)
    opc = int(input('Qual aluno você quer saber as notas?(999 interrompe) '))
    if opc == 999:
        print('Finalizando...')
        sleep(1.5)
        break
    if opc <= len(ficha)-1:
        print(f'As notas do aluno {ficha[opc][0]} foram {ficha[opc][1]}')
print('\033[1;32m<<< Volte sempre! >>>\033[m')