# Leia a velocidade de um carro, se passar de 80km/h, será multado R$7,00 por km excedente.

# determina a velocidade do carro
velocidade = float(input('Informe a qual velocidade, em km/h, você dirigia: '))

# determina o valor da multa por km
multa = (velocidade - 80) * 7

# determina limite de velocidade
if velocidade > 80:
    print(f'Você está acima da velocidade permitida! Você receberá uma multa de R${multa:.2f}! ')
print('Tenha um bom dia, boa viagem! ;) ')
