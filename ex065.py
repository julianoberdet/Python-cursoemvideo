resp = 'S'
media = soma = qtd = maior = menor = 0
while resp in 'Ss':
    n = int(input('Digite um número: '))
    soma += n
    qtd += 1
    if qtd == 1:
        maior = menor = n
    else:
        if n > maior:
            maior = n
        if n < menor:
            menor = n
    resp = str(input('Deseja continuar?[S/N] ')).upper().strip()[0]
media = soma / qtd
print(f'Você digitou {qtd} números e a media deles é {media:.2f}!')
print(f'O maior foi {maior} e o menor foi {menor}')


