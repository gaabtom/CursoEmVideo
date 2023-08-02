# Leia um número inteiro qualquer e peça para o usuário escolher qual será
# a base de conversão: 1 para binário; 2 para octal; 3 para hexadecimal.

num = int(input('Digite um número inteiro: '))
print('[ 1 ] Converter para BINÁRIO.')
print('[ 2 ] Converter para OCTAL.')
print('[ 3 ] Converter para HEXADECIMAL.')
opção = int(input('Sua opção: '))

if opção == 1:
    print(f'A conversão de {num} para binário é igual a {bin(num)[2:]}.')
elif opção == 2:
    print(f'A conversão de {num} para octal é igual a {oct(num)[2:]}.')
elif opção == 3:
    print(f'A conversão de {num} para hexadecimal é igual a {hex(num)[2:]}.')
else:
    print('Opção inválida! Reinicie o programa e tente novamente.')