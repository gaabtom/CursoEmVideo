# Desafio 018 - Faça um programa que leia um ângulo qualquer e mostre o valor do seno, cosseno e tangente.
from math import sin, cos, tan, radians
angulo = float(input('Digite o valor de um ângulo: '))
radianos = radians(angulo)
print(f'Com base no ângulo {angulo}:\nSeu seno é: {sin(radianos):.2f};\nSeu cosseno é: {cos(radianos):.2f};\nSua tangente é {tan(radianos):.2f}. ')



