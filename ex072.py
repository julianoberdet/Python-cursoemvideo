contagem = ('zero','um','dois','três','quatro','cinco','seis','sete','oito','nove','dez','onze',
'doze','treze','catorze','quinze','dezesseis','dezessete','dezoito','dezenove','vinte')
while True:
    numero = int(input('Digite um número entre 0 e 20: '))
    if 0 <= numero <= 20:
        print(f'O número digitado foi \033[32;4m{contagem[numero]}\033[m')
        resp = ' '
        while resp not in 'SN':
            resp = str(input('Você quer continuar?[S/N] ')).strip().upper()[0]
        if resp == 'N':
            break
    else:
        print('\033[31;1mTente novamente', end=' -> \033[m')
#Coloquei um enquanto sim ou não no exercicio