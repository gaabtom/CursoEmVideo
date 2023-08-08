# Refaça o DESAFIO 009, mostrando a tabuada de um número que o usuário escolher, utilizando
# um laço for.

n = int(input('Digite um número para ver sua tabuada: '))
for c in range(1, 11):
    print(f'{n} X {c} = {n * c}')