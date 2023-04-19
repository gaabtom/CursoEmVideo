# Leia a velocidade de um carro, se passar de 80km/h, será multado R$7,00 por km excedente.

velocidade = float(input('A quantos KM seu carro está rodando na estrada? '))
multa = (velocidade - 80) * 7
if velocidade >80:
    print(f'Você está andando acima da velocidade permitida de 80km/h.\nPor isso, será cobrada uma multa de R$7 por KM excedente.\nSendo assim, você pagará R${multa:.2f}.')
else:
    print('Continue em frente! Não ultrapasse a velocidade permitida.')
