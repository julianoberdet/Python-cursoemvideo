#Escreva um programa que pergunte o salário de um funcionário e calcule o valor do seu aumento.
#Para salários superiores a R$ 1250,00 , calcule um aumento de 10%. Para inferiores ou iguais, o aumento
#é de 15%.

salario = float(input('Digite seu salário:R$ '))
if salario <= 1250.00:
    aumento = salario + (salario * 0.15)
else:
    aumento = salario + (salario * 0.10)
print(f'Seu salário é {salario:.2f} e após o reajuste vai ficar R${aumento:.2f}')
