'''Faça um programa que leia nome e peso de várias pessoas, guardando tudo em uma lista. No final, mostre:
a) quantas pessoas foram cadastradas.
b) uma listagem com as pessoas mais pesadas.
c) uma listagem com as pessoas mais leves.'''

turma = []
dados = []
peso = []
while True:
    dados.append(str(input('Nome: ')))
    dados.append(float(input('Peso: ')))
    turma.append(dados[:])
    peso.append(dados[1])
    dados.clear()
    maior = max(peso)
    menor = min(peso)
    escolha = ' '
    while escolha not in 'SN':
        escolha = str(input('Deseja continuar? [S/N] ')).strip().upper()[0]
    if escolha == 'N':
        break
print('-=' * 30)
print(f'Ao todo, você cadastrou {len(turma)} pessoas.')
print(f'O menor peso foi {menor}Kg. Peso de ', end='')
for pessoa in turma:
    if pessoa[1] == menor:
        print(f'[{pessoa[0]}]', end=' ')
print(f'\nO maior peso foi {maior}Kg. Peso de', end=' ')
for pessoa in turma:
    if pessoa[1] == maior:
        print(f'[{pessoa[0]}]', end=' ')
