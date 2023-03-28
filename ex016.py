# Desafio 016 - Crie um programa que leia um número real qualquer e mostre sua porção inteira.
from math import trunc
number = float(input('Digite um número: '))
print(f'A parte inteira de {number} é {trunc(number)}.')


