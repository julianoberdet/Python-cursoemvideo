n1 = int(input('Primeiro valor: '))
n2 = int(input('Segundo valor: '))
if n1 > n2:
    print('O \033[32mPRIMEIRO\033[m valor é maior.')
elif n2 > n1:
    print('O \033[33mSEGUNDO\033[m valor é maior.')
else:
    print('Os dois valores são \033[34mIGUAIS\033[m.')