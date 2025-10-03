nome = str(input('Qual seu primeiro nome? ')).strip()
if nome == 'Juliano':
    print('Que nome bonito!')
elif nome == 'Maria' or nome == 'Paulo' or nome == 'Pedro':
    print('Seu nome é bem popular no Brasil.')
elif nome in 'Ana Juliana Patricia Julia':
    print('Belo nome feminino!')
else:
    print('Seu nome é bem normal.')
print(f'Tenha um bom dia, {nome}!')