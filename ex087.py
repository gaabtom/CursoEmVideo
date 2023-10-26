'''Aprimore o desafio anterior, mostrando no final:
a) a soma de todos os valores pares digitados
b) a soma dos valores da terceira coluna
c) o maior valor da segunda linha'''

somapares = somacoluna = maiorlinha = 0
matriz = [0, 0, 0], [0, 0, 0], [0, 0, 0]
for linha in range(0, 3):
    for coluna in range(0, 3):
        matriz[linha][coluna] = int(input(f'Digite um valor para {[linha, coluna]}: '))
print('-=' * 30)
for linha in range(0, 3):
    for coluna in range(0, 3):
        print(f'[{matriz[linha][coluna]:^5}]', end='')
        if matriz[linha][coluna] % 2 == 0:
            somapares += matriz[linha][coluna]
    print()
print('-=' * 30)
print(f'A soma dos valores pares é igual a {somapares}.')
for linha in range(0, 3):
    somacoluna += matriz[linha][2]
print(f'A soma dos valores da terceira coluna é igual a {somacoluna}.')
for coluna in range(0, 3):
    if coluna == 0:
        maiorlinha = matriz[1][coluna]
    if matriz[1][coluna] > maiorlinha:
        maiorlinha = matriz[1][coluna]
print(f'O maior valor da segunda linha é {maiorlinha}.')
