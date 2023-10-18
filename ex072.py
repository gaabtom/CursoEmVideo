'''Crie um programa que tenha uma tupla totalmente preenchida com uma contagem por extenso,
de zero até vinte. O programa deve ler um número pelo teclado (entre 0 e 20) e mostrar por extenso.'''

numeros = ('zero', 'um', 'dois', 'três', 'quatro', 'cinco', 'seis',
           'sete', 'oito', 'nove', 'dez', 'onze', 'doze', 'treze', 'quatorze', 'quinze', 'dezesseis',
           'dezessete', 'dezoito', 'dezenove', 'vinte')
while True:
    escolha = int(input('Digite um número de 0 a 20: '))
    if 0 <= escolha <= 20:
        break
    print('Tente novamente. ', end='')
print(f'O número digitado foi {numeros[escolha]}.')
