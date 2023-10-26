'''Crie um programa que leia nome e duas notas de vários alunos e guarde tudo em uma lista composta. No final,
mostre um boletim contendo a média de cada um e oermita que o usuário possa mostrar as notas de cada aluno.'''

lista = []
while True:
    nome = str(input('Nome: '))
    nota1 = float(input('Nota 1: '))
    nota2 = float(input('Nota 2: '))
    media = (nota1 + nota2) / 2
    lista.append([nome, [nota1, nota2], media])
    escolha = ' '
    while escolha not in 'SN':
        escolha = str(input('Deseja continuar? [S/N] ')).upper().strip()[0]
    if escolha == 'N':
        break
print('-' * 30)
print(f'{"N°":<4}{"Nome":<10}{"Média":>8}')
for indice, aluno in enumerate(lista):
    print(f'{indice:<4}{aluno[0]:<10}{aluno[2]:>8.1f}')
while True:
    print('-' * 25)
    opcao = int(input('Deseja mostrar as notas de qual aluno? (999 para interromper): '))
    if opcao <= len(lista) - 1:
        print(f'As notas de {lista[opcao][0]} são {lista[opcao][1]}.')
    if opcao == 999:
        print('FINALIZANDO...')
        break
print('<<< VOLTE SEMPRE >>>')
