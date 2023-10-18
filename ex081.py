'''Crie um programa que vai ler vários números e colocar em uma lista. Depois disso, mostre:
a) Quantos números foram digitados
b) A lista de valores, ordenada de forma decrescente
c) Se o valor 5 foi digitado e está ou não na lista.'''
numeros = []
while True:
    numeros.append(int(input(f'Digite um número: ')))
    numeros.sort(reverse=True)
    escolha = ' '
    while escolha not in 'SN':
        escolha = str(input('Deseja continuar? [S/N] ')).strip().upper()[0]
    if escolha == 'N':
        break
print('-=' * 30)
print(f'Você digitou {len(numeros)} números.')
print(f'A lista em ordem descrescente dos números é {numeros}')
if 5 in numeros:
    print('O valor 5 foi encontrado na lista.')
else:
    print('O valor 5 não foi encontrado na lista.')
