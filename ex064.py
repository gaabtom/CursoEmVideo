'''Crie um programa que leia vários números inteiros pelo teclado. O programa só vai parar quando
o usuário digitar o valor 999, que é a condição de parada. No final, mostre quantos números foram
digitados e qual foi a soma entre eles (desconsiderando o flag - 999).'''

num = contador = soma = 0
while num != 999:
    num = int(input(f'Digite o {contador + 1}° número [999 para parar]: '))
    if num != 999:
        contador += 1
        soma += num
print(f'Programa encerrado. Foram digitados {contador} números, e a soma entre eles é {soma}.')

