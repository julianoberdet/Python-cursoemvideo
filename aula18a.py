#Exemplo
galera = []
dado = []
totmaior = totmenor = 0
for c in range(0,3):
    dado.append(str(input('Nome: ')))
    dado.append(int(input('Idade: ')))
    galera.append(dado[:])
    dado.clear()
print(galera)
for p in galera:
    if p[1] > 21:
        print(f'{p[0]} é maior de idade')
        totmaior += 1
    else:
        print(f'{p[0]} é menor de idade')
        totmenor += 1
print(f'Na lista tem {totmaior} maiores de idade e {totmenor} menores de idade')






#Outro exemplo
'''galera = [['João',19],['Maria', 33],['Joaquim',45],['Pedro', 22]]
print(galera[0]) #['João',19]
print(galera[0][0]) #Só o João
print(galera[2][1]) #Só o 45
for p in galera:
    print(p) #Aparece todas listas dentro da lista
    print(p[0]) #Aparece só o 0 de cada lista
    print(f'O {p[0]} tem {p[1]} anos') #Mostra o indice 0 e 1'''



#Exemplo prático
'''teste = list()
teste.append('Juliano')
teste.append(32)
galera = list()
galera.append(teste[:])
teste[0] = 'Maria'
teste[1] = 25
galera.append(teste[:])
print(galera)'''