# Pergunte o salário de um funcionário, e calcule o valor do seu aumento.
# Para salários superiores a R$1250, calcule um aumento de 10%.
# Para inferiores ou iguais, o aumento é de 15%.

salário = float(input('Qual é o seu salário em R$? '))
if salário >=1250:
    print(f'Parabéns! Seu amuento será de 10%, totalizando R${(salário/100) * 10 + salário:.2f}! ')
else:
    print(f'Parabéns! Seu aumento será de 15%, totalizando R${(salário/100) * 15 + salário:.2f}! ')

