'''Crie um programa que leia dois valores e mostre um menu na tela:
[1] somar
[2] multiplicar
[3] maior
[4] novo números
[5] sair do programa
Seu programa deverá realizar a operação solicitada em cada caso.'''
from time import sleep

escolha = 0
num1 = int(input('Digite um número: '))
num2 = int(input('Digite outro número: '))
while escolha != 5:
    print('-=' * 15)
    print('''    [ 1 ] Somar
    [ 2 ] Multiplicar
    [ 3 ] Maior Número
    [ 4 ] Gerar novos números
    [ 5 ] Sair''')
    escolha = int(input('Digite sua escolha: '))
    if escolha == 1:
        soma = num1 + num2
        print(f'A soma entre {num1} e {num2} é igual a {soma}!')
    elif escolha == 2:
        mult = num1 * num2
        print(f'A multiplicação entre {num1} e {num2} é igual a {mult}!')
    elif escolha == 3:
        if num1 > num2:
            maior = num1
        else:
            maior = num2
        print(f'Entre {num1} e {num2} o maior é {maior}!')
    elif escolha == 4:
        num1 = int(input('Digite um número novamente: '))
        num2 = int(input('Digite mais um número: '))
    elif escolha == 5:
        print('Finalizando...')
sleep(2)
print('-=' * 15)
print('Fim do programa! Volte sempre!')

