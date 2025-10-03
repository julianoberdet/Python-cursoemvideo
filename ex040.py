#Crie um programa que eia duas notas de um aluno e calcule sua média, mostrando uma mensagem
#no final, de acordo com a média atingida: abaixo de 5.0 reprovado,media entre 5 e 6.9 recuperação
#media 7.0 ou superior aprovado.

n1 = float(input('Primeira nota: '))
n2 = float(input('Segunda nota: '))
m = (n1 + n2) / 2
if m < 5.0:
    print('Você foi \033[31mREPROVADO\033[m!')
elif m == 5.0 < 7.0:
    print('Você está em \033[33mRECUPERAÇÃO\033[m!')
else:
    print('Você está \033[32mAPROVADO\033[m!')