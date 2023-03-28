# Desafio 022 - Crie um programa que leia um nome completo e mostre:
# - o nome com todoas as letras maiúsculas e minúsculas;
# - quantas letras ao total sem contar espaços;
# - quantas letras tem o primeiro nome.

nome = input('Digite seu nome completo: ').strip()
cada_nome = nome.split()
sem_espaços = ''.join(cada_nome)
print('Maiúsculo:', nome.upper())
print('Minúsculo:', nome.lower())
print('Quantidade de letras:', len(sem_espaços))
print('Quantidade de letras do primeiro nome:', len(cada_nome[0]))







