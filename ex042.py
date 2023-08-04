# Refaça o DESAFIO 35, acrescentando o recurso de mostrar que tipo de
# triangulo será formado:
# Equilátero: todos os lados iguais;
# Isósceles: dois lados iguais;
# Escaleno: todos os lados diferentes.

r1 = float(input('Informe o comprimento da primeira reta: '))
r2 = float(input('Da segunda reta: '))
r3 = float(input('Da terceira reta: '))

if r1 < r2 + r3 and r2 < r1 + r3 and r3 < r1 + r2:
    print('As retas \033[1;32mpodem\033[m formar um triângulo!')
    if r1 == r2 == r3:
        print('O triângulo é \033[1;32mEQUILÁTERO\033[m!')
    elif r1 == r2 or r2 == r3 or r3 == r1:
        print('O triângulo é \033[1;32mISÓSCELES\033[m!')
    elif r1 != r2 != r3 != r1:
        print('O triângulo é \033[1;32mESCALENO\033[m!')
else:
    print('As retas \033[1;31mnão podem\033[m formar um triângulo.')
