'''lanche = ('Hamburger','Suco','Pizza','Bolo')
#lanche[1] = 'Refrigerante' TUPLAS SÃO IMUTAVEIS
print(lanche[1])'''

#Modos de usar for com tuplas
'''lanche = ('Hamburger','Suco','Pizza','Bolo','Batata frita')

for comida in lanche:  #Jeito mais simples, mas sem saber a posição
   print(f'Eu comi {comida}')

for cont in range(0 , len(lanche)): #Jeito marcando posição
    print(f'eu vou comer {lanche[cont]} na posição {cont}')

for  pos, comida in enumerate(lanche):  #Outro jeito marcando posição
    print(f'Vou comer {comida} na posição {pos}')
print('Comi pra caramba')'''

#Para ordenar a tupla em ordem alfabética
'''lanche = ('Hamburger','Suco','Pizza','Bolo','Batata frita')
print(sorted(lanche))
print(lanche)'''

#Outro jeito em tuplas
a = (2,5,4)
b = (5,8,1,2)
c = a + b
print(c) # (2,5,4,5,8,1,2) ele junta a com b, se fosse b+a, inverte os números
#print(c.count(5)) #conta quantos numeros 5 tem
print(c.index(8)) #Em que posição está o 8
