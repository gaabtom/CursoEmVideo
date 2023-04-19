# Leia 3 números, mostre qual o maior e o menor.

num1 = int(input('Digite um número: '))
num2 = int(input('Digite outro número: '))
num3 = int(input('Por fim, mais um número: '))

lista = [num1, num2, num3]

print(f'O maior número é {max(lista)}, e o menor é {min(lista)}.')
