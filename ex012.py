# Faça um algoritmo que leia o preço de um produto e gere outro com 5% de desconto.

p = float(input('Qual é o valor do produto? R$'))
d = p - (5 * p / 100)
print(f'Parabéns! O produto de R${p:2f} recebeu um desconto de 5%! Agora, está de R${d:.2f}. Boas compras!')




