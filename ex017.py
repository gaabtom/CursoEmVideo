# Desafio 017 - Faça um programa que leia o comprimento do cateto oposto e do adjacente de um triângulo retângulo, calcule e mostre a hipotenusa. *utilizar módulos*
from math import hypot
cateto_oposto = float(input('Digite o comprimento do cateto oposto: '))
cateto_adjacente = float(input('Agora, digite o cateto adjacente: '))
print(f'A hipotenusa de um triângulo retângulo com o cateto oposto de {cateto_oposto}, e o adjacente de {cateto_adjacente}, sua hipotenusa é {hypot(cateto_oposto, cateto_adjacente):.2f}. ')
