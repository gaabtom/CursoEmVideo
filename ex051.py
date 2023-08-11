# Desenvolva um programa que leia o primeiro termo e a razão de uma Progressão Aritmética.
# No final, mostre os 10 primeiros termos dessa progressão.

# Lê o primeiro termo e a razão
n1 = int(input('Indique o primeiro termo da progressão: '))
raz = int(input('Indique a razão da progressão: '))

# Determina o décimo termo
décimo = n1 + (10 - 1) * raz

# Mostra na tela os 10 primeiros termos, de acordo com a estrutura for (primeiro termo, décimo termo + razão, razão)
print('Os 10 primeiros termos da progressão são:')
for c in range(n1, décimo + raz, raz):
    print(f'{c}', end=' -> ')
print('Acabou!')
