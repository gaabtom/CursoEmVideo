'''Faça um programa que leia nome e média de um aluno, guardando também a situação (menos de 7, reprovado),
em um dicionário. No final, mostre o conteúdo da estrutura na tela.'''

aluno = dict()
aluno['Nome'] = str(input('Nome: '))
aluno['Média'] = float(input(f'Média de {aluno["Nome"]}: '))
if aluno['Média'] >= 7:
    aluno['Situação'] = 'Aprovado'
if aluno['Média'] < 5:
    aluno['Situação'] = 'Reprovado'
if 5 <= aluno['Média'] < 7:
    aluno['Situação'] = 'Recuperação'
print('-=' * 30)
for k, v in aluno.items():
    print(f'- {k} é igual a {v}.')


