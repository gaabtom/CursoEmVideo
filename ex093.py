'''Crie um programa que gerencie o aproveitamento de um jogador de futebol. O programa vai ler o nome do
jogador e quantas partidas ele jogou. Depois, vai ler a quantidade de gols feitos em cada partida. No final,
tudo isso será guardado em um dicionário, incluindo o total de gols feitos durante o campeonato.'''

listagols = list()
dados = dict()
soma = 0
dados['Nome'] = str(input('Nome do Jogador: '))
quantpartidas = int(input(f'Quantas partidas {dados["Nome"]} jogou? '))
for c in range(quantpartidas):
    listagols.append(int(input(f'Quantos gols na partida {c+1}? ')))
dados['Gols'] = listagols
dados['Total'] = sum(listagols)
print('-=' * 30)
print(dados)
print('-=' * 30)
for k, v in dados.items():
    print(f'O campo {k} tem o valor {v}.')
print('-=' * 30)
print(f'O jogador {dados["Nome"]} jogou {quantpartidas} partidas.')
for i, v in enumerate(dados['Gols']):
    print(f'    => Na partida {i+1}, fez {v} gols.')
print(f'Foi um total de {dados["Total"]} gols.')
