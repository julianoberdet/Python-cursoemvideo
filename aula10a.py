'''tempo = int(input('Quantos anos tem seu carro? '))
if tempo <= 3:
    print('Carro Novo')
else:
    print('Carro Velho')
print('--FIM--')'''


'''  #CONDIÇÃO SIMPIFICADA
tempo = int(input('Quantos anos tem seu carro? '))
print('carro novo'if tempo <=5 else'carro velho')
print('--FIM--')'''


'''nome = str(input('Digite seu primeiro nome: ')).strip().upper()
if nome == 'JULIANO':
    print('Que nome lindo você tem!')
print(f'Bom dia, {nome}!!')'''


n1 = float(input('Digite a nota da A1: '))
n2 = float(input('Digite a nota da A2: '))
n3 = float(input('Digite a nota da A3: '))
m = ((n1 * 0.30) + (n2 * 0.40) + (n3 * 0.30))
print(f'Sua média é {m:.1f}!')
if m >= 7:
    print('-✅  Você foi aprovado, Parabéns! -')
else:
    print('-❌ Você foi reprovado, estude mais da próxima vez! -')
print(':📚: UniRitter Campus Pelotas :📚:')