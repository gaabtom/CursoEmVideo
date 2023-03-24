# Faça um algoritmo que leia o preço de um produto e gere outro com 5% de desconto.

p = float(input('Qual é o valor do produto (R$)?'))
cent = (5*p)/100
d = p-cent
print(f'Parabéns! O produto de R${p} recebeu um desconto de 5%! Agora, está de R${d:.2f}. Boas compras!')


