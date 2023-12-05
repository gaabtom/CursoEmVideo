'''Aprimore o DESAFIO 93 para que ele funcione com vários jogadores, incluindo um sistema de visualização de
detalhes do aproveitamento do jogador'''

time = list()
jogador = dict()
gols = list()
while True:
    gols.clear()
    jogador['Nome'] = str(input('Nome do jogador: '))
    partidas = int(input(f'Quantas partidas {jogador["Nome"]} jogou? '))
    for p in range(partidas):
        gols.append(int(input(f'Quantos gols na partida {p+1}? ')))
    jogador['Gols'] = gols[:]
    jogador['Total'] = sum(gols)
    time.append(jogador.copy())
    while True:
        escolha = str(input('Deseja continuar? [S/N] ')).upper().strip()[0]
        if escolha in 'SN':
            break
        print('ERRO! Por favor, digite apenas S ou N.')
    if escolha == 'N':
        break

print('-=' * 30)
print('Cód', end='')
for elementos in jogador.keys():
    print(f'{elementos:<15}', end='')
print()
print('-' * 40)
for k, v in enumerate(time):
    print(f'{k:>3} ', end='')
    for dados in v.values():
        print(f'{str(dados):<15}', end='')
    print()
print('-' * 40)
while True:
    opc = int(input('Mostrar dados de qual jogador? (999 para parar) '))
    if opc == 999:
        break
    if opc >= len(time):
        print(f'ERRO! Não existe o jogador {opc}!')
    else:
        print(f'  -- LEVANTAMENTO DO JOGADOR {time[opc]["Nome"]}')
        for i, g in enumerate(time[opc]['Gols']):
            print(f'   No jogo {i+1} fez {g} gols.')
    print('-' * 40)
print(f'<< VOLTE SEMPRE >>')
