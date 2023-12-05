'''Faça um programa que tenha uma função chamada escreva(), que receba um texto qualquer como um parâmetro e mostre uma mensagem
com tamanho adaptável.'''


def escreva(txt):
    tam = len(txt) + 4
    print('~' * tam)
    print(txt.center(tam))
    print('~' * tam)


# Programa principal
msg = str(input('Digite uma mensagem para ser formatada: '))
escreva(msg)

