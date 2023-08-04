# Leia o peso e a altura de uma pessoa, calcule seu IMC e mostre seu status:
# Abaixo de 18.5: Abaixo do peso;
# Entre 18.5 e 25: Peso ideal;
# 25 até 30: Sobrepeso;
# 30 até 40: Obesidade;
# Acima de 40: Obesidade mórbida.

peso = float(input('Digite seu peso: (Kg) '))
altura = float(input('Digite sua altura: (m) '))

imc = peso / (altura ** 2)

print(f'Seu IMC é de \033[1;33m{imc:.1f}\033[m!')

if imc < 18.5:
    print('Você está \033[1;31mABAIXO DO PESO\033[m.')
elif imc <= 25:
    print('Você está com o \033[1;32mPESO IDEAL\033[m!')
elif imc <= 30:
    print('Você está em \033[1;31mSOBREPESO\033[m.')
elif imc <= 40:
    print('Você está em \033[1;31mOBESIDADE\033[m.')
else:
    print('Você está em \033[1;31mOBESIDADE MÓRBIDA\033[m.')
