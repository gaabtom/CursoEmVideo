'''Melhore o jogo do desafio 028 onde o computador vai "pensar" em um númeroentre 0 e 10.
Só que agora o jogador vai tentar adivinhar até acertar,
mostrando quantas tentativas foram necessárias para vencer.'''

# Importa da bilioteca random a função randint
from random import randint

# Gera um número aleatório entre 0 e 10
num_maq = randint(0, 10)

# Mostra na tela uma mensagem e pergunta o palpite do jogador
print('-=' * 25)
print('Estou pensando em um número entre 0 e 10...')
print('-=' * 25)
tent = int(input('Qual é seu palpite? '))

# Define o número de palpites igual a 1
palp = 1

# Enquanto o número gerado pela máquina for diferente do palpite, gera mais uma tentativa
# Mostrando "mais que isso" se for menor ou "menos que isso" se for maior
# Adiciona +1 ao número de palpites a cada tentativa
while num_maq != tent:
    if tent < num_maq:
        tent = int(input('Mais que isso! Tente novamente: '))
        palp += 1
    if tent > num_maq:
        tent = int(input('Menos que isso! Tente novamente: '))
        palp += 1

# Mostra na tela uma mensagem de parabéns e a quantidade de palpites
print(f'Parabéns! Você acertou com {palp} tentativas.')