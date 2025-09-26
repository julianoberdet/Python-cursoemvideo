#Escreva um programa que pergunte o salário de um funcionário e calcule o valor do seu aumento.
#Para salários superiores a R$ 1250,00 , calcule um aumento de 10%. Para inferiores ou iguais, o aumento
#é de 15%.

salario = float(input('Digite seu salário:R$ '))
aumento = salario + (salario * 0.10)
if salario > 1250.00:
    print(f'Seu salário após o reajuste será de R${aumento:.2f}')
else:
    print(f'Seu salário após o reajuste vai ficar R${salario + (salario*0.15):.2f}')
