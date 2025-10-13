#Crie um programa que leia uma frase qualquer e diga se ela é um palindromo, desconsiderando
#os espaços. ex: Apos a casa, A sacada da casa, a torre da derrota , O lobo ama o bolo

frase = str(input('Digite uma frase: ')).strip()
frase_limpa = frase.replace(' ', '').lower()
invertida = ''
for c in range(len(frase_limpa) -1, -1, -1):
    invertida += frase_limpa[c]
print(frase_limpa)
if frase_limpa == invertida:
        print('A frase é um palindromo')
else:
        print('A frase não é um palindromo')
