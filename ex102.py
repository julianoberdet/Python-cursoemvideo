def fatorial(n=1,show=False):
    """
    -> Calcular o fatorial de um número
    :param n: O número a ser calculado
    :param show: (opcional) se quer que apareça o calculo
    :return: retorna o valor do fatorial
    """
    print('-' * 40)
    m = 1
    for c in range(n,0,-1):
        m *= c
        if show:
            print(c,end=' ')
            if c > 1:
                print('x',end=' ')
            else:
                print('=',end=' ')
    return m


#Programa principal
print(fatorial(5,show=True))