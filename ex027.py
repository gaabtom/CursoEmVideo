# Desafio 027 - Faça um programa que leia um nome completo e mostre o primeiro e último nome separadamente.
# Ex.: Ana Maria de Souza
# Primeiro = Ana
# último = Souza

nome = input('Digite seu nome completo: ')
dividido = nome.split()
print(f'Seu primeiro nome é {dividido[0]};\nSeu último nome é {dividido[-1]}.')


