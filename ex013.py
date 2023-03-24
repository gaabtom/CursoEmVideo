# Desafio 013 - Faça um algoritmo que leia o salário de um funcionário e acrescente 15% de aumento.

nome = input('Bem-Vindo ao algoritmo de sua empresa. Qual o seu nome?')
s = int(input(f'Olá, {nome}! Digite seu salário atual (R$):'))
cent = (15*s)/100
a = s+cent
print(f'Uau, parabéns {nome}! O patrão decidiu que seu salário de R${s} agora receberá um aumento de 15%, ganhando R${a}!')
