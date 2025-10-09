#Crie um programa que eia duas notas de um aluno e calcule sua média, mostrando uma mensagem
#no final, de acordo com a média atingida: abaixo de 5.0 reprovado,media entre 5 e 6.9 recuperação
#media 7.0 ou superior aprovado.

n1 = float(input('Primeira nota: '))
n2 = float(input('Segunda nota: '))
m = (n1 + n2) / 2
print(f'Tirando a nota {n1:.1f} e {n2:.1f} o aluno ficou com a média {m:.1f}!')
if m < 5.0:
    print('O aluno está \033[31mREPROVADO\033[m!')
elif 6.9 >= m >= 5:
    print('O aluno está em \033[33mRECUPERAÇÃO\033[m!')
else:
    print('O aluno está \033[32mAPROVADO\033[m!')