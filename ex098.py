from time import sleep
def contador(i,f,p):
    if p < 0:
        p *= -1
    if p == 0:
        p = 1
    print('-=' * 30)
    print(f'A contagem de {i} até {f} de {p} em {p} ')
    if i <= f:
        cont = i
        while cont <= f:
            print(f'{cont} ',end='')
            sleep(0.5)
            cont += p
        print('FIM!')
    else:
        cont= i
        while cont >= f:
            print(f'{cont} ',end='')
            sleep(0.5)
            cont -= p
        print('FIM!')


def personalizado():
    print('-=' * 30)
    print('Agora é sua vez de personalizar:')
    inicio = int(input('INICIO: '))
    fim = int(input('FIM: '))
    passo = int(input('PASSO: '))
    contador(inicio,fim,passo)


#Programa principal
contador(1,10,1)
contador(10,0,2)
personalizado()