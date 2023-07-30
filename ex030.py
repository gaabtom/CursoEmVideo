# Leia se um número é par ou ímpar

# determina o número
num = int(input('Digite um número: '))

# se o resto da divisão de (num) por 2 = 0, o número será par, se não, ímpar
if (num % 2) == 0:
    print('O número é par!')
else:
    print('O número é ímpar!')
