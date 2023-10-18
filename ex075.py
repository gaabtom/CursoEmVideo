'''Desenvolva um programa que leia 4 valores pelo teclado e guarde-os em uma tupla. No final, mostre:
a) quantas vezes apareceu o número 9
b) em que posição foi digitado o primeiro valor 3
c) quais foram os números pares'''

numeros = int(input('Digite um número: ')), int(input('Digite outro número: ')),\
    int(input('Digite mais um número: ')), int(input('Digite o último número: '))
print(f'Você digitou os valores: {numeros}')
print(f'O valor 9 apareceu {numeros.count(9)} vezes')
if 3 in numeros:
    print(f'O valor 3 apareceu na {numeros.index(3)+1}ª posição')
else:
    print(f'O valor 3 não foi digitado em nenhuma posição')
print('Os valores pares digitados foram ', end='')
for pares in numeros:
    if pares % 2 == 0:
        print(pares, end=' ')
