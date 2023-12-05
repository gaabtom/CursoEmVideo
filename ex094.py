'''Crie um programa que leia nome, sexo e idade de várias pessoas, guardando os dados de cada pessoa em um dicionário e todos
os dicionários em uma lista. No final, mostre:
a) Quantas pessoas foram cadastradas
b) A média de idade do grupo
c) Uma lista com todas as mulheres
d) Uma lista com todas as pessoas com idade acima da média'''

pessoas = dict()
total = list()
mulheres = list()
somaidades = media = quantidades = 0
while True:
    pessoas['Nome'] = str(input('Nome: '))
    pessoas['Sexo'] = str(input('Sexo [M/F]: ')).upper().strip()[0]
    while pessoas['Sexo'] not in 'MF':
        print('ERRO! Por favor digite apenas M ou F.')
        pessoas['Sexo'] = str(input('Sexo [M/F]: ')).upper().strip()[0]
    if pessoas['Sexo'] == 'F':
        mulheres.append(pessoas['Nome'])
    pessoas['Idade'] = int(input('Idade: '))
    quantidades += 1
    somaidades += pessoas['Idade']
    total.append(pessoas.copy())
    print(pessoas)
    escolha = str(input('Deseja continuar? [S/N] ')).strip().upper()[0]
    while escolha not in 'SN':
        print('ERRO! Por favor digite apenas S ou N.')
        escolha = str(input('Deseja continuar? [S/N] ')).strip().upper()[0]
    if escolha == 'N':
        break
print('-=' * 30)
print(f'A) O grupo tem {len(total)} pessoas.')
media = somaidades / len(total)
print(f'B) A média de idades é de {media:5.2f} anos.')
print(f'C) As mulheres cadastradas foram:', end=' ')
for i, v in enumerate(mulheres):
    print(f'{v} ', end='')
print()
print(f'D) Lista das pessoas que estão acima da média: ')
for pessoas in total:
    if pessoas['Idade'] >= media:
        for k, v in pessoas.items():
            print(f'{k} = {v};', end=' ')
        print()
print('<< ENCERRADO >>')
