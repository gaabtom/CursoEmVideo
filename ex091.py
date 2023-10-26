'''Crie um programa onde 4 jogadores joguem um dado e obtenham resultados aleatórios. Guarde esses resultado
em um dicionário. No final, coloque esse dicionário em ordem, sabendo que o vencedor tirou o maior número
no dado.'''

# Importa biblioteca para gerar números aleatórios
from random import randint

# Importa biblioteca para esperar um tempo entre os prints
from time import sleep

# Inicializa o dicionário 'jogo'
jogo = dict()

# Adiciona os jogadores(1-4) dentro do dicionário jogo, cada jogador recebe um n° entre 1 e 6 aleatório
jogo['Jogador1'] = randint(1, 6)
jogo['Jogador2'] = randint(1, 6)
jogo['Jogador3'] = randint(1, 6)
jogo['Jogador4'] = randint(1, 6)

# Representação visual
print(f'-=' * 5, ' < JOGANDO DADOS >', '-=' * 5)

# inicia um loop for para mostrar de forma organizada as keys (jogador(1-4)) e os valores (n°s 1 a 6)
for k, v in jogo.items():
    print(f'O {k} tirou {v} no dado.')

    # utiliza o método sleep para pausar os prints de 1 em 1 segundos
    sleep(1)

# Inicializa a variável cont para armazenar o contador de posições do ranking
cont = 1

# Representação visual
print(f'  {" RANKING ":=^30}  ')

# Inicia um loop for que para (jogador) orgazina (sorted) o dicionário (jogo),
# pegando a chave (key=jogo.get), e mostrando seu reverso (reverse=True)
for jogador in sorted(jogo, key=jogo.get, reverse=True):

    # Mostra na tela que o (contador = 1°) lugar foi (jogador - parâmetro usado na
    # repetição, que pega todas as chaves (jogador(1-4)) que estão em jogo) que tirou (jogo = dicionário na
    # posição (jogador) definida pelo loop
    print(f'O {cont}° lugar foi {jogador} que tirou {jogo[jogador]}')

    # Adiciona 1 ao contador a cada loop
    cont += 1

    # Utiliza o método sleep para pausar os prints de 1 em 1 segundos
    sleep(1)

# Representação visual de encerramento
print('<<< FIM DO JOGO >>>')
