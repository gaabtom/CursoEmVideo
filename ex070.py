'''Crie um programa que leia o nome e o preço de vários produtos. O programa deverá perguntar se o usuário
vai continuar. No final, mostre:
a) qual é o total gasto na compra
b) quantos produtos custam mais de R$1000
c) qual é o nome do produto mais barato'''

total = maisdemil = menorpreço = cont = 0
nomebarato = ' '
while True:
    produto = str(input('Digite o nome do produto: '))
    preço = int(input('Digite seu preço: R$'))
    cont += 1
    total += preço
    if preço > 1000:
        maisdemil += 1
    if cont == 1 or preço < menorpreço:
        menorpreço = preço
        nomebarato = produto
    continuar = ' '
    while continuar not in 'SN':
        continuar = str(input('Quer continuar? [S/N]')).strip().upper()[0]
    if continuar == 'N':
        break
print('{:-^40}'.format(' FIM DO PROGRAMA '))
print(f'O total gasto foi de R${total:.2f}.')
print(f'A quantidade de produtos que custaram mais de R$1000 foi {maisdemil}.')
print(f'O produto mais barato foi {nomebarato} e custou R${menorpreço}.')
