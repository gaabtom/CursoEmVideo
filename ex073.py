'''Crie uma tupla preenchida com os 20 primeiros colocados da Tebela do Campeonato Brasileiro de Futebol,
na ordem de colocação. Depois mostre:
a) apenas os 5 primeiros colocados
b) os últimos 4 colocados da tabela
c) uma lista com os times em ordem alfabética
d) em que posição na tabela está o time do fluminense.'''

times = ('Botafogo', 'Bragantino', 'Grêmio', 'Palmeiras', 'Flamengo', 'Fortaleza', 'Fluminense', 'Athletico-PR', 'Atlético-MG', 'São Paulo', 'Cuiabá', 'Internacional', 'Corinthians', 'Santos', 'Cruzeiro', 'Bahia', 'Vasco da Gama', 'Goiás', 'Coritiba', 'América-MG')
print('=' * 40)
print(f'Lista de times do Brasileirão: {times}')
print('=' * 40)
print(f'Os 5 primeiros são: {times[0:5]}')
print('=' * 40)
print(f'Os 4 últimos são: {times[-4:]}')
print('=' * 40)
print(f'Times em ordem alfabética: {sorted(times)}')
print('=' * 40)
print(f'O time do fluminense está na {times.index("Fluminense")+1}ª posição')
