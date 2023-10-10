'''Crie um programa que leia vários números inteiros pelo teclado. No final da execução, mostre a média
entre todos os valores e qual foi o maior e o menor valores lidos. O programa deve perguntar ao usuário
se ele quer ou não continuar a digitar valores.'''

num = contador = soma = media = maior = menor = 0
escolha = 'S'
while escolha not in 'Nn':
    num = int(input('Digite um número: '))
    escolha = str(input('Deseja continuar? [S/N] ')).upper().strip()[0]
    contador += 1
    soma += num
    if contador == 1:
        maior = menor = num
    else:
        if num > maior:
            maior = num
        if num < menor:
            menor = num
media = soma / contador
print(f'Você digitou {contador} números. A média entre eles é {media:.2f}.')
print(f'O maior valor digitado foi {maior} e o menor foi {menor}.')
