#Listas e dicionários
jogador = {}
partida = []
principal = []

#Cadastro de jogadores
while True:
    jogador.clear()
    jogador['nome'] = str(input('Nome do jogador: '))
    tot = int(input(f'Quantas partidas {jogador["nome"]} jogou? '))
    partida.clear()
    for c in range(0,tot):
        partida.append(int(input(f'  Quantos gols fez na {c+1}ª partida? ')))
    jogador['gols'] = partida[:]
    jogador['total'] = sum(jogador['gols'])
    principal.append(jogador.copy())

#Pergunta se deseja continuar
    while True:
        resp = str(input('Quer continuar[S/N]? ')).upper()[0]
        if resp in 'SN':
            break
        print('ERRO! Responda apenas S ou N')
    if resp == 'N':
        break

#Exibição da tabela de jogadores
print('-=' * 30)
print('cod' , end='')
for i in jogador.keys():
    print(f' {i:<15} ',end='')
print()
print('-' * 50)
for k, v in enumerate(principal):
    print(f'{k:>3} ', end='')
    for d in v.values():
        print(f'{str(d):<18}',end='')
    print()
print('-' * 50)

#Consulta detalhada por jogador
while True:
    opc = int(input('mostrar dado de qual jogador?(999 interrompe) '))
    if opc == 999:
        break
    if opc >= len(principal):
        print(f'ERRO! Não existe jogador com número {opc}')
    else:
        print(f'--- LEVANTAMENTO DO JOGADOR {principal[opc]["nome"]} ---')
        for i, l in enumerate(principal[opc]["gols"]):
            print(f'    No jogo {i+1} fez {l} gols')
        print(f'=> Total de {principal[opc]["total"]} gols')
    print('-' * 40)
print(' <<< VOLTE SEMPRE >>>')
