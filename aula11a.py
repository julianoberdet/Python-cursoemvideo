#print('\033[7;33;44mOlá, mundo!\033[m')

#n1 = 2
#n2 = 4
#print(f'Os valores são \033[32m{n1}\033[m e \033[31m{n2}\033[m!!!')

#nome = 'Juliano'
#print(f'Muito prazer em te conhecer \033[34m{nome}\033[m!')

nome = str(input('Digite seu primeiro nome: '))
cores = {'limpa': '\033[m',
         'azul': '\033[34m',
        'amarelo': '\033[33m',
         'pretoebranco': '\033[7;38m'}
print(f'Muito prazer em te conhecer {cores['pretoebranco']}{nome}{cores['limpa']} !!')

