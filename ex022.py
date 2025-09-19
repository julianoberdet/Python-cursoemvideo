#Crie um programa  que leia o nome completo de uma pessoa e mostre: O nome com todas
#letras maiusculas,o nome com todas letras minusculas, quantas letras ao todo, sem
# considerar espaços, quantas letras tem o primeiro nome

nome = str(input('Digite seu nome completo: ')).strip()
print('Analisando o seu nome...')
print(f'Seu nome em letras maiusculas {nome.upper()}')
print(f'Seu nome em letras minusculas {nome.lower()}')
print(f'O seu nome completo contem {len(nome) - nome.count(' ')} letras!')
separa =  nome.split()
#print(f'o primeiro nome é {separa[0]} e ele tem {nome.find(' ')} letras!') pode ser também
print(f'Seu primeiro nome é {separa[0]} e contem {len(separa[0])} letras')

