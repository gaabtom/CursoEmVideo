'''Crie um programa que gerencie o aproveitamento de um jogador de futebol. O programa vai ler o nome do
jogador e quantas partidas ele jogou. Depois, vai ler a quantidade de gols feitos em cada partida. No final,
tudo isso será guardado em um dicionário, incluindo o total de gols feitos durante o campeonato.'''

listagols = list()
dados = dict()
soma = 0
dados['Nome'] = str(input('Nome do Jogador: '))
quantpartidas = int(input(f'Quantas partidas {dados["Nome"]} jogou? '))
for c in range(quantpartidas):
    gols = (int(input(f'Quantos gols na partida {c+1}? ')))
    soma += gols
    listagols.append(gols)
dados['Gols'] = listagols
dados['Total'] = soma
print('-=' * 30)
print(dados)
print('-=' * 30)
for k, v in dados.items():
    print(f'O campo {k} tem o valor {v}.')
print('-=' * 30)
print(f'O jogador {dados["Nome"]} jogou {quantpartidas} partidas.')
for i in range(quantpartidas):
    print(f'    => Na partida {i+1}, fez {dados["Gols"][i]} gols.')
