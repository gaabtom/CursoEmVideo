# Desafio 010 - Crie um programa que mostra quanto dinheiro uma pessoa tem na carteira e quantos dólares ela pode comprar. U$1,00 = R$3,27

nome = input('Olá, Bem-Vindo(a) a sua Carteira Digital! Qual é o seu nome?')
n = float(input(f'Ok, {nome}, qual é seu valor (R$) em carteira?'))
d = n/3.27
print(f'Certo! Com seu valor de R${n}, você conseguirá comprar U${d:.2f} dólares.')









