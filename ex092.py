'''Crie um programa que leia nome, ano de nascimento e carteira de trabalho de uma pessoa e cadastre (com a
idade) em um dicionário, se a CTPS for diferente de ZERO, o dicionário receberá também o ano de contratação
e o salário. Calcule e acrescente, além da idade, com quantos anos a pessoa vai se aposentar.
Aponsentar = 35 anos de trabalho.'''

from datetime import date
infos = dict()
infos['Nome'] = str(input('Nome: '))
nascimento = int(input('Ano de nascimento: '))
anoatual = date.today().year
infos['Idade'] = anoatual - nascimento
infos['Ctps'] = int(input('Carteira de trabalho (0 se não tiver): '))
if infos['Ctps'] != 0:
    infos['Contratação'] = int(input('Ano de contratação: '))
    infos['Salário'] = float(input('Salário: R$'))
    anoaposentadoria = infos['Contratação'] + 35
    infos['Aposentadoria'] = anoaposentadoria - nascimento
print('-=' * 30)
for k, v in infos.items():
    print(f' - {k} tem o valor {v}')
