# Desafio 023 - Faça um programa que leia um num. de 0 a 9999 e mostre cada um dos dígitos separados.
# Ex.: Digite um número: 1834
# unidade: 4
# dezena: 3
# centena: 8
# milhar: 1

num = input('Digite um número: ')
print('Unidade:', num[3])
print('Dezena:', num[2])
print('Centena:', num[1])
print('Milhar:', num[0])

