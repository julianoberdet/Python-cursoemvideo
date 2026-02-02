def fatorial(n=1,show=False):
    """
    ->Calcula o valor fatorial de um número
    :param n: O número a ser calculado
    :param show: (opcional) Mostrar ou não a conta
    :return: O valor fatorial de um número
    """
    print('-' * 40)
    m = 1
    for c in range(n,0,-1):
        m *= c
        if show:
            print(c,end=' ')
            print('x' if c > 1 else '=',end=' ')
    return m


#Programa principal
print(fatorial(5,show=True))