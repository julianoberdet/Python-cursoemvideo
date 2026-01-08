#EXEMPLO 1
'''pessoas = {'nome': 'Juliano', 'sexo':'M', 'idade': 32}
print(f'O {pessoas["nome"]} tem {pessoas["idade"]} anos') #nome e idade referenciados tem que usar ""
# por que está dentro de aspas simples
#Para declarar usa-se {} e para referenciar usa-se []
print(pessoas.keys())
print(pessoas.values())
print(pessoas.items())
del pessoas['sexo'] #Para apagar algo
pessoas['nome'] = 'Leandro' #Se eu quiser modificar o elemento
pessoas['peso'] = 87.9
for k, v  in pessoas.items():
    print(f'{k} - {v}')'''

''''#EXEMPLO 2
brasil = []
estado1 = {'uf': 'Rio Grande do Sul', 'sigla':'RS'}
estado2 = {'uf': 'Alagoas', 'sigla':'AL'}
brasil.append(estado1)
brasil.append(estado2)
print(brasil)
print(brasil[1]['uf'])
print(brasil[0]['sigla'])'''

#EXEMPLO3
estado = dict()
brasil = list()
for c in range(0,3):
    estado['uf'] = str(input('Unidade Federativa: '))
    estado['sigla'] = str(input('Sigla do Estado: '))
    brasil.append(estado.copy())
for e in brasil:
    #for k, v in e.items():
       # print(f'O campo {k} tem valor {v}.')
    for v in e.values():
        print(v,end=' ')
    print()
