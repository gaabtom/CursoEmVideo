'''Faça um programa que laia 5 valores numéricos e guarde-os em uma lista. No final, mostre qual foi o maior
e o menor valor digitado e as suas respectivas posições na lista.'''

valores = []
for c in range(0, 5):
    valores.append(int(input(f'Digite o {c+1}° valor: ')))
maior = max(valores)
menor = min(valores)
print('-=' * 30)
print(f'Você digitou os valores: {valores}')
print(f'O maior valor digitado foi {maior}, que está nas posições ', end='')
for indice, valor in enumerate(valores):
    if valor == maior:
        print(f'{indice}...', end=' ')
print(f'\nO menor valor digitado foi {menor}, que está na posições ', end='')
for indice, valor in enumerate(valores):
    if valor == menor:
        print(f'{indice}...', end=' ')

