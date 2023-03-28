# Desafio 020 - O mesmo professor do desafio anterior quer sortear a ordem de apresentação de trabalhos.
# Faça um programa que leia o nome dos quatro alunos e mostre a ordem sorteada.
from random import shuffle
a1 = str(input('Digite o nome do aluno um: '))
a2 = str(input('Digite o nome do aluno dois: '))
a3 = str(input('Digite o nome do aluno três: '))
a4 = str(input('Digite o nome do aluno quatro: '))
lista = [a1, a2, a3, a4]
shuffle(lista)
print(f'A ordem de apresentação de trabalho será:\n {lista}')





