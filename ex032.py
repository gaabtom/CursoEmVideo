# Leia se um ano qualquer é bissexto ou não.

ano = int(input('Digite um ano: '))
if (ano%4)== 0 and (ano%100)!= 0 or (ano%4)==0 and (ano%100)==0 and (ano%400)== 0:
    print('Esse é um ano bissexto! Que legal!')
else:
    print('Esse ano não é bissexto. Meh.')
    