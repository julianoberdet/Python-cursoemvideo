def leiaInt(msg):
    ok = False
    valor = 0
    while True:
        n = str(input('Digite um número: '))
        if n.isnumeric():
            valor = int(n)
            ok = True
        else:
            print('\033[1;31mERRO! Digite novamente um número.\033[m')
        if ok:
            break
    return valor


# Programa principal
n = leiaInt('Digite um número: ')
print(f'O número digitado foi {n}')