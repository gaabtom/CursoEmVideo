''' Faça um programa que leia um número inteiro e diga se ele é ou não número primo.
(Divisível apenas por 1 e por ele mesmo).'''

# Lê o número.
num = int(input('Digite um número: '))

# Apresenta o quantidade de números divisíveis.
divisivel = 0

# Estrutura de repetição for que faz a contagem de 1 até o número digitado.
for c in range(1, num + 1):
    # Se o número apresentado no intervalo for dívisivel pelo n. digitado, aparece em amarelo.
    if num % c == 0:
        divisivel += 1
        print(f'\033[33m{c}\033[m', end=' ')
    # Se não for, aparece em vermelho.
    else:
        print(f'\033[31m{c}\033[m', end=' ')
# Mostra na tela a quantidade de números que o n. digitado é divisível.
print(f'\nO número {num} foi divisível {divisivel} vezes!')

if divisivel > 2:
    # Se essa quantidade for maior que 2, não é primo.
    print('E por isso, ele NÃO É PRIMO!')
elif divisivel == 2:
    # Se for igual a 2, é primo.
    print('E por isso, ele É PRIMO!')
