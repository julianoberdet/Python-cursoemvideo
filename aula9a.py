'''Fatiamento de string
-Analise
len() le quantos caracteres
count() conta
find() vai dizer em qua caractere começa o 'deo' por exemplo no 11
in diz se é verdadeiro ou falso

-Transformação
replace() substitui uma palavra por outra
upper() coloca em letra maiusculas
lower() coloca em letras minusculas
capitalize() a primeira letra maiuscula e o resto minusculas
title() começo de cada palavra com letra maiuscula
strip() remove espaços inuteis
rstrip() remove espaços da direita apenas
lstrip() remove espaços da esquerda apenas

-Divisão
split() cada uma das  palavras é colocada dentro de um aoutra lista

-Junção
.join() junta, exemplo '-'.join(frase.split()))

'''

#frase = 'Curso em video Python'
#print(frase[3])
#print(frase[3:13])
#print(frase[:13])
#print(frase[:21])
#print(frase[13:])
#print(frase[9:21:2])
#print(frase[9:21:3])

#frase = ('Curso em video Python')
#print(len(frase))

#frase = ('Curso em video python')
#print(frase.count('o'))

#frase = ('Curso em video Python')
#print(frase.find('deo'))

#frase = ('Curso em video Python')
#print(frase.find('android')) #vai dar -1 por que não tem na frase

#frase = ('Curso em video Python')
#print('Curso' in frase)

#frase = ('Curso em video Python')
#print(frase.replace('Python','Android'))

#frase = ('Curso em video Python')
#print(frase.upper()) #Maiusculas
#print(frase.lower()) #Minusculas
#print(frase.capitalize())
#print(frase.title())

#frase = ('   Aprenda Python  ')
#print(frase.strip()) #Remove os espaços inuteis

#frase = ('   Aprenda Python  ')
#print(frase.rstrip()) #Tira os espaços da direita
#print(frase.lstrip()) #Tira os espaços da esquerda

#frase = ('Curso em video Python')
#print(frase.split())
#print('-'.join(frase.split()))

#print("""A página inicial é, sem sombra de dúvidas, a página mais importante de seu site.
#É ela quem vai realizar o primeiro contato com o visitante, e é por isso mesmo que ela
#requer uma atenção especial de quem a administra. Sendo assim, o ideal é que todas as
#informações sejam claras e fáceis de entender. Ou seja, não é legal usar termos técnicos
#demais, ou colocar detalhes desnecessários. Diga o que sua empresa faz, como faz e como
#pode ajudar o consumidor.""")

#frase = '   Curso em video Python      '
#print(frase.upper().count('O'))
#print(frase.lower().count('c'))
#print(len(frase.strip()))

#frase = 'Curso em video Python'
#frase = frase.replace('Python','Java')
#print(frase,len(frase))

frase = 'Curso em Video Python'
print(frase.lower().find('video'))
dividido = frase.split()
print(dividido[0]) #Mostra só a primeira palavra;
print(dividido[0][2]) #Mostra a letra 2 da primeira palavra;
print('-'.join(frase.split())) #colocar traços em cada palavra;