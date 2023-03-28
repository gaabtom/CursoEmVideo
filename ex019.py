# Desafio 019 - Um professor quer sortear um dos seus quatro alunos para apagar o quadro.
# Faça um programa que leia o nome deles e escreva o sorteado.
from random import choice
aluno1 = input('Digite o nome dos primeiro aluno: ')
aluno2 = input('Digite o nome do segundo aluno: ')
aluno3 = input('Digete o nome do terceiro aluno: ')
aluno4 = input('Digite o nome do quarto aluno: ')
lista = [aluno1, aluno2, aluno3, aluno4]
sorteio = choice(lista)
print(f'O aluno que deverá apagar o quadro é {sorteio}!')
