'''Crie um programa que vai ler vários números e colocar em uma lista. Depois disso, crie duas listas
extras que vão conter apenas os valores pares e os valores ímpares digitados, respectivamente. Ao final,
mostre o contéudo das três listas geradas.'''

lista = []
pares = []
impares = []
while True:
    n = (int(input('Digite um número: ')))
    lista.append(n)
    if n % 2 == 0:
        pares.append(n)
    else:
        impares.append(n)
    escolha = ' '
    while escolha not in 'SN':
        escolha = str(input('Deseja continuar? [S/N] ')).strip().upper()[0]
    if escolha == 'N':
        break
print('-=' * 30)
print(f'A lista completa é {lista}')
print(f'A lista de números pares é {pares}')
print(f'A lista de números ímpares é {impares}')
