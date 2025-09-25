#Escreva um programa que faça o computador "pensar" em um número de 0 a 5 e peça para o usuário
#tentar descobrir qual foi o número escolhido pelo computador. O programa deverá escrever na tela
#se o usuário venceu ou perdeu


import random
n = random.randint(0,5)
print('Vamos sortear um número de 0 a 5')
print(f'O número escolhido foi: {n}')
if n >=3:
    print('Você é o ganhador!! 😃')
else:
    print('Você perdeu! 😞')
print('Muito obrigado, até o próximo sorteio!')
