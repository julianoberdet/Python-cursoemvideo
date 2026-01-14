galera = []
pessoa = {}
soma = media = 0

#Leitura dos dados
while True:
    pessoa.clear() #A cada vez que o loop voltar apaga a pessoa
    pessoa['nome'] = str(input('Nome: '))

    #SEXO apenas M ou F
    while True:
        pessoa['sexo'] = str(input('Sexo[M/F]: ')).upper()[0]
        if pessoa['sexo'] in 'FM':
            break
        print('ERRO! Responda apenas M ou F.')
    pessoa['idade'] = int(input('Idade: '))
    soma += pessoa['idade'] # Para somar as idades

    #Colocar o dicionario dentro da lista galera
    galera.append(pessoa.copy())

    #Dar só sim ou não
    while True:
        resp = str(input('Quer continuar[S/N]? ')).upper()[0]
        if resp in 'SN':
            break
        print('ERRO! Responda apenas S ou N')
    if resp == 'N':
        break

#Analise dos dados
print('-=' * 30)
print(f' A) Ao todo foram {len(galera)} pessoas cadastradas')
media = soma / len(galera)
print(f' B) A média de idade é de {media:5.2f} anos')
print(f' C) As mulheres cadastradas foram: ',end='')
for p in galera:
    if p['sexo'] == 'F':
        print(f'[{p['nome']}] ',end='')
print()
print(' D) Lista das pessoas que estão acima da média: ')
for p in galera:
    if p['idade'] >= media:
        print('     ',end='')
        for k,v in p.items():
            print(f' {k} = {v} ',end='')
        print()
print('<<< ENCERRANDO >>>')








#Jeito que eu fiz
'''cadastro = {}
lista = []
somaidade = 0
mulher = []
while True:
    cadastro['nome'] = str(input('Nome: '))
    cadastro['sexo'] = ' '
    while cadastro['sexo'] not in 'MF':
        cadastro['sexo'] = str(input('Sexo[M/F]: ')).upper()[0]
        if cadastro['sexo'] not in 'MF':
            print('ERRO! Responda apenas M ou F')
    cadastro['idade'] = int(input('Idade: '))
    lista.append(cadastro.copy())
    somaidade += cadastro['idade']

    if cadastro['sexo'] == 'F':
        mulher.append(cadastro['nome'])

    resp = ' '
    while resp not in 'SN':
        resp = str(input('Quer continuar[S/N]? ')).upper()[0]
        if resp not in 'SN':
            print('ERRO! Responda apenas S ou N')
    if resp == 'N':
        break
mediaidade = somaidade / len(lista)
print('-=' * 30)
print(f'A) Foram cadastradas {len(lista)} pessoas')
print(f'B) A media de idade é {mediaidade:.2f}')
print(f'C) As mulheres cadastradas foram {mulher}')
print(f'D) Lista de pessoas que estão acima da media:')
for p in lista:
    if p['idade'] > mediaidade:
        print(f'    Nome = {p["nome"]}; Sexo = {p["sexo"]}; Idade = {p["idade"]} ')'''

