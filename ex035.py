# Leia o comprimento de três retas e diga ao usuário se elas podem ou não formar um triângulo.

r1 = float(input('Informe o comprimento da primeira reta: '))
r2 = float(input('Informe o comprimento da segunda reta: '))
r3 = float(input('Informe o comprimento da terceira reta: '))
soma = r1 + r2
if soma > r3:
    print(f'Com as retas informadas, é possível formar um triângulo, que legal! ;) ')
else:
    print(f'Que pena! As retas informadas não formam um triângulo. :( ')
