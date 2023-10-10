'''Crie um programa que leia a idade e sexo de várias pessoas. A cada pessoa cadastrada, o programa deverá
perguntar se o usuário quer ou não continuar, no final, mostre:
a) a quantidade de pessoas com mais de 18 anos.
b) quantos homens foram cadastrados.
c) quantas mulheres tem menos de 20 anos.'''

maioridade = homem = mulheres20 = 0
while True:
    print('-' * 30)
    print('CADASTRE UMA PESSOA')
    print('-' * 30)
    idade = int(input('Qual é a sua idade? '))
    sexo = ' '
    while sexo not in 'MF':
        sexo = str(input('Informe seu sexo: [M/F] ')).upper().strip()[0]
    if idade >= 18:
        maioridade += 1
    if sexo == 'M':
        homem += 1
    if idade < 20 and sexo == 'F':
        mulheres20 += 1
    continuar = ' '
    while continuar not in 'NS':
        continuar = str(input('Quer continuar? [S/N] ')).strip().upper()[0]
    if continuar == 'N':
        break
print('-' * 30)
print(f'Total de pessoas com mais de 18 anos: {maioridade}.')
print(f'Ao todo temos {homem} homens cadastrados.')
print(f'E temos {mulheres20} mulheres com menos de 20 anos.')
