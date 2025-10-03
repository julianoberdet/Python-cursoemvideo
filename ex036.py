#Escreva um programa para aprovar o empréstimo bancário para a compra de uma casa. O programa
#vai perguntar o valor da casa, o salário do comprador e em quantos anos ele vai pagar.
#Calcule o valor da prestação mensal, sabendo que ela não pode exceder 30% do salário ou então
#o empréstimo será negado.

casa = float(input('Qual o valor da casa?R$ '))
salario = float(input('Qual o seu salário?R$ '))
anos = int(input('Quantos anos quer pagar: '))
prestacao = (casa / 12) / anos



