'''Crie um programa que tenha uma tupla com várias palavras (não usar acentos). Depois disso, você deve
mostrar, para cada palavra, quais são suas vogais.'''

palavras = ('programar', 'aprender', 'python', 'curso', 'video', 'trabalhar', 'praticar',
            'ensinar', 'assistir', 'transformar', 'educar', 'revolucionar', 'futuro')
for p in palavras:
    print(f'\nNa palavra {p.upper()} temos ', end='')
    for letra in p:
        if letra in 'aeiou':
            print(letra, end=' ')
