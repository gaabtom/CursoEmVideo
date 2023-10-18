'''Crie um programa onde o usuário possa digitar vários valores uméricos e cadastre-os em uma lista.
Caso o número já exista la dentro, ele não será adicionado. No final, serão exibidos todos os
valores únicos digitados, em ordem crescente.'''

nums = []
while True:
    n = int(input('Digite um número: '))
    if n not in nums:
        print('Valor adiconado com sucesso...')
        nums.append(n)
    else:
        print('Valor duplicado! Não vou adicionar...')
    escolha = ' '
    if escolha not in 'SN':
        escolha = str(input('Deseja continuar? [S/N] ')).strip().upper()[0]
    if escolha == 'N':
        break
print('-=' * 30)
print(f'Os números digitados foram {sorted(nums)}')
