# Crie um programa que jogue pedra, papel e tesoura com você.

from time import sleep
from random import choice

print('''Suas opções:
[ 0 ] PEDRA
[ 1 ] PAPEL
[ 2 ] TESOURA''')

jogada = int(input('Qual é a sua jogada? '))

print('JO...')
sleep(1)
print('KEN...')
sleep(1)
print('PO!!!')

lista = ['Pedra', 'Papel', 'Tesoura']

jogada_computador = choice(lista)

print('-=' * 15)
print(f'Computador jogou {jogada_computador}!')
if jogada == 0:
    print(f'Jogador jogou Pedra!')
elif jogada == 1:
    print(f'Jogador jogou Papel!')
elif jogada == 2:
    print('Jogador jogou Tesoura!')
else:
    print('JOGADA INVÁLIDA!')
print('-=' * 15)
if jogada == 0 and jogada_computador == 'Pedra':
    print('EMPATE!')
elif jogada == 0 and jogada_computador == 'Papel':
    print('COMPUTADOR VENCE!')
elif jogada == 0 and jogada_computador == 'Tesoura':
    print('JOGADOR VENCE!')
elif jogada == 1 and jogada_computador == 'Papel':
    print('EMPATE!')
elif jogada == 1 and jogada_computador == 'Pedra':
    print('JOGADOR VENCE!')
elif jogada == 1 and jogada_computador == 'Tesoura':
    print('COMPUTADOR VENCE!')
elif jogada == 2 and jogada_computador == 'Tesoura':
    print('EMPATE!')
elif jogada == 2 and jogada_computador == 'Pedra':
    print('COMPUTADOR VENCE!')
elif jogada == 2 and jogada_computador == 'Papel':
    print('JOGADOR VENCE!')
