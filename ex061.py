'''Refaça o desafio 51, lendo o primeiro termo e a razão de uma PA,
mostrando os 10 primeiros termos da progressão usando estrutura while.'''
print('Gerador de PA')
print('-=' * 15)
t1 = int(input('Digite o primeiro termo da PA: '))
raz = int(input('Digite a razão: '))
termos = t1
contador = 1
while contador <= 10:
    print(f'{termos} -> ', end='')
    termos += raz
    contador += 1
print('FIM.')