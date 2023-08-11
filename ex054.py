''' Crie um programa que leia o ano de nascimento de sete pessoas. No final, mostre quantas
Pessoas ainda não atingiram a maioridade e quantas já são maiores. Maioridade = 21 anos. '''

from datetime import date

# Determina os valores de maior e menor idade, e o ano atual
maioridade = 0
menoridade = 0
atual = date.today().year

# Utiliza da estrutura for para gerar 7 anos diferentes, e dita a idade da pessoa
for faixa in range(1, 8):
    ano = int(input(f'Digite o ano de nascimento da {faixa} pessoa: '))
    idade = atual - ano
    # Se a idade for maior ou igual a 21, adiciona 1 à maioridade, se não, adiciona à menoridade
    if idade >= 21:
        maioridade += 1
    else:
        menoridade += 1

# Imprime na tela a quantidade de maiores e menores de idade
print(f'A quantidade de pessoas maiores de idade é de {maioridade}, e de menores é {menoridade}.')
