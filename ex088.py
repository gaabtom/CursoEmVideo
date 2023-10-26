'''Faça um programa que ajude um jogador da MEGA SENA a criar palpites. O programa vai parguntar quantos
jogos serão gerados e vai sortear 6 números entre 1 e 60 para cada jogo, cadastrando em uma lista composta.'''

from random import randint
from time import sleep
palpitestemporarios = []
jogos = []
print('-' * 30)
print(F'{"JOGA NA MEGA SENA":^30}')
print('-' * 30)
quant = int(input('Quantos jogos você quer que eu sorteie? '))
tot = 1
while tot <= quant:
    cont = 0
    while True:
        num = randint(1, 60)
        if num not in palpitestemporarios:
            palpitestemporarios.append(num)
            cont += 1
        if cont == 6:
            break
    palpitestemporarios.sort()
    jogos.append(palpitestemporarios[:])
    palpitestemporarios.clear()
    tot += 1
print('-=' * 3, f'SORTEANDO {quant} JOGOS', '-=' * 3)
for indice, lista in enumerate(jogos):
    print(f'Jogo {indice+1}: {lista}')
    sleep(1)
print('-=' * 5, ' < BOA SORTE > ', '-=' * 5)
