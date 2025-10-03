#Desenvolva uma lógica que leia o peso e a altura de uma pessoa, calcule sei IMC e mostre seu
#status, de acordo com a tabela abaixo:
'''Abaixo de 18.5: abaixo do peso
---Entre 18.5 e 25: peso ideal
---25 até 30: Sobrepeso
---30 até 40: Obesidade
---Acima de 40: Obesidade mórbida'''

peso = float(input('Qual é o seu peso? '))
altura = float(input('Qual é sua altura? '))
imc = peso / (altura * altura)
if imc < 18.5:
    print(f'Seu imc é {imc:.1f} e você está Abaixo do peso')
elif imc >= 18.5 and imc <= 25:
    print(f'Seu imc é {imc:.1f} e você está com peso ideal')
elif imc >= 25 and imc <= 30:
    print(f'Seu imc é {imc:.1f} e você está com sobrepeso.')
elif imc >= 30 and imc <= 40:
    print(f'Seu imc é {imc:.1f} e você está na faixa de obesidade')
else:
    print(f'Seu imc é {imc:.1f} e você está com obesidade mórbida')