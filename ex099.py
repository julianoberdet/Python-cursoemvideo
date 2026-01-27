from time import sleep
def maior(*num):
    cont = maior = 0
    print('-=' * 30)
    print(f'Analizando os valores passados:')
    for valor in num:
        print(f'{valor} ',end='')
        sleep(0.3)
        if cont == 0:
            maior = valor
        else:
            if valor > maior:
                maior = valor
        cont+=1
    print(f'Foram informados {cont} valores ao todo')
    print(f'O maior valor informado foi {maior}')


#programa principal
maior(1, 2, 6, 3, 8)
maior(5, 9, 8)
maior(1, 2)
maior(6)
maior()