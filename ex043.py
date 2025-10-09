#Desenvolva uma lógica que leia o peso e a altura de uma pessoa, calcule sei IMC e mostre seu
#status, de acordo com a tabela abaixo:
'''Abaixo de 18.5: abaixo do peso
---Entre 18.5 e 25: peso ideal
---25 até 30: Sobrepeso
---30 até 40: Obesidade
---Acima de 40: Obesidade mórbida'''

peso = float(input('Qual é o seu peso?(Kg) '))
altura = float(input('Qual é sua altura?(m) '))
imc = peso / (altura ** 2)
print(f'Seu imc é {imc:.1f}')
if imc < 18.5:
    print('Você está ABAIXO DO PESO')
elif 18.5 <= imc < 25:
    print('Você está com PESO IDEAL')
elif 25 <= imc < 30:
    print('Você está com SOBREPESO.')
elif 30 <= imc < 40:
    print('Você está na faixa de OBESIDADE')
else:
    print('Você está com OBESIDADE MÓRBIDA')