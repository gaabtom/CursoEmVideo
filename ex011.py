# Desafio 011 - Faça um programa que leia a largura e altura de uma parede em metros,
# e calcule sua área e quantidade de tinta necessária para pintá-la, sabendo que cada litro de tinta pinta uma área de 2m².

la = float(input('Qual é a largura da parede em metros?'))
a = float(input('E a altura em metros?'))
ar = la * a
lt = ar / 2
print(f'Sua parede tem a dimensão de {la}x{a} e sua área é de {ar}m².\nPara pintá-la, você precisará de {lt} litros de tinta.')




