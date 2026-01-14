from datetime import datetime
cadastro = {}
cadastro['nome'] = str(input('Nome: '))
nasc = int(input('Ano de nascimento: '))
cadastro['idade'] = datetime.now().year - nasc
cadastro['ctps'] = int(input('Carteira de Trabaho (0 NÃO TEM): '))
if cadastro['ctps'] != 0:
    cadastro['ano de contratação'] = int(input('Ano de contratação: '))
    cadastro['salário'] = float(input('Salário:R$ '))
    cadastro['Aposentadoria'] = cadastro['idade'] + ((cadastro['ano de contratação'] + 35) - datetime.now().year)
print('-=' * 30)
for k,v in cadastro.items():
    print(f'{k} tem o valor {v}')
