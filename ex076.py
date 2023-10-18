'''Crie um programa que tenha uma tupla única com nomes de produtos e seus respectivos preços, na sequência.
No final, mostre uma listagem de preços, organizando os dados em forma tabular'''

produtos = ('Lápis', 1.75,
            'Borracha', 2,
            'Caderno', 15.90,
            'Estojo', 10.50,
            'Transferidor', 4.25,
            'Compasso', 7.99,
            'Mochila', 120.75,
            'Canetas', 21.40,
            'Livro', 45.50)
print('-' * 40)
print(f'{"LISTAGEM DE PRODUTOS":^40}')
print('-' * 40)
for posição in range(0, len(produtos)):
    if posição % 2 == 0:
        print(f'{produtos[posição]:.<30}', end='')
    else:
        print(f'R${produtos[posição]:>7}')
print('-' * 40)
