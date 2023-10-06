'''Faça um programa que leia um número qualquer e mostre seu fatorial.'''

n = int(input('Digite um número para saber seu fatorial: '))
contador = n
fatorial = 1
print(f'Calculando {n}! = ', end='')
while contador > 0:
        print(f'{contador}', end='')
        print(f' x ' if contador > 1 else ' = ', end='')
        fatorial *= contador
        contador -= 1
print(f'{fatorial}')



'''print(f'O fatorial de {n} é igual a {contador}!')'''