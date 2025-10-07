numero = int(input('Digite um número: '))
print('''Escolha uma das bases para conversâo: 
[ 1 ] converter para BINÁRIO
[ 2 ] converter para OCTAL
[ 3 ] converter para HEXADECIMAL''')
opção = int(input('Digite sua opção: '))
if opção == 1:
    print(f'{numero} convertido para BINÁRIO é {bin(numero)[2:]}')
elif opção == 2:
    print(f'{numero} convertido para OCTAL é {oct(numero)[2:]}')
elif opção == 3:
    print(f'{numero} convertido para HEXADECIMAL é {hex(numero)[2:]}')
else:
    print('Opção inválida, Tente novamente!!')
