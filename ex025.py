# Desafio 025 - Crie um programa que leia um nome e diga se contém 'SILVA'.

nome = input('Digite seu nome: ').strip()
dividido = nome.upper().split()
print('O nome digitado contém "SILVA"?', 'SILVA' in dividido)
