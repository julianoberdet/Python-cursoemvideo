'''def mostraLinha():
    print('-' * 50)


mostraLinha()
print('                Sistema de Alunos       ')
mostraLinha()'''

'''def titulo(txt):
    print('-' * 30)
    print(txt)
    print('-' * 30)

#PROGRAMA PRINCIPAL
titulo('       Curso em video     ')
titulo('       Aprenda Python     ')
titulo('       Gustavo Guanabara  ')'''

'''def soma(a,b):
    print(f'A = {a} e B = {b}')
    s = a + b
    print(f'A soma de A + B é {s}')


#Programa Principal
soma(4,5)
soma(8,9)
soma(1,2)'''

'''#EXEMPLO DE EMPACOTAMENTO
def contador(*num):
    tam = len(num)
    print(f'Recebi os valores {num}  e ao todo são {tam} números')
    print('-' * 60)

contador(2,4,1)
contador(3,2)
contador(2,4,6,7,8)'''

#Outro exemplo
def dobra(lst):
    pos = 0
    while pos < len(lst):
        lst[pos] *= 2
        pos += 1

valores = [6 , 3 , 9 , 1, 0 ,2 ]
dobra(valores)
print(valores)