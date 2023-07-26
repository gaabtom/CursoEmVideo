# Leia a velocidade de um carro, se passar de 80km/h, será multado R$7,00 por km excedente.

velocidade = float(input('Informe a qual velocidade, em km/h, você dirigia: '))
multa = (velocidade - 80) * 7
if velocidade > 80:
    print(f'Você está acima da velocidade permitida! Você receberá uma multa de R${multa}! ')
else:
    print('Tudo certo! Boa viagem! ;) ')
