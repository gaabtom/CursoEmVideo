# Escreva um programa que pergunte a quantidade de km rodados por um carro alugado e a quantidade de dias alugada. Calcule o preço, sabendo que o carro custa R$60 por dia e R$0.15 por km rodado.

d = int(input('Quantos dias alugados?'))
km = float(input('Quantos Km rodados?'))
print(f'O total a pagar é R${(d * 60) + (km * 0.15):.2f}.')


