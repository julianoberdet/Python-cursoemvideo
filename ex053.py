#Crie um programa que leia uma frase qualquer e diga se ela é um palindromo, desconsiderando
#os espaços. ex: Apos a casa, A sacada da casa, a torre da derrota , O lobo ama o bolo

#Correção do Guanabara
frase = str(input('Digite uma frase: ')).strip().upper()
palavras = frase.split()
junto = ''.join(palavras)
inverso = junto[::-1]
print(f'O inverso de {junto} é {inverso}')
if inverso == junto:
    print('Temos um palíndromo!')
else:
    print('A frase digitada não é um palíndromo!')

#Jeito que eu tinha feito
'''frase = str(input('Digite uma frase: ')).strip().upper()
frase_limpa = frase.replace(' ', '')
invertida = ''
for c in range(len(frase_limpa) -1, -1, -1):
    invertida += frase_limpa[c]
print(f'O inverso de {frase_limpa} é {invertida}')
if frase_limpa == invertida:
        print('A frase é um palindromo')
else:
        print('A frase não é um palindromo')'''
