'''Melhore o DESAFIO 061, perguntando para o usuário se ele quer mostrar mais alguns termos.
 O programa encerra quando ele disser que quer mostrar 0 termos.'''

print('Gerador de PA')
print('-=' * 15)
primeiro_termo = int(input('Digite o primeiro termo da PA: '))
razao = int(input('Digite a razão: '))
contador = 1
mais = 10
total = 0
while mais != 0:
    total += mais
    while contador <= total:
        print(f'{primeiro_termo} -> ', end='')
        primeiro_termo += razao
        contador += 1
    print('PAUSA')
    mais = int(input('Quantos termos quer adicionar na PA? '))
print(f'Progressão aritmética finalizada. Foram exibidos um total de {contador - 1} termos.')

