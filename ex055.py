# Faça um programa que leia o peso de cinco pessoas. No final, mostre o maior e o menor peso de todos.

# Define o maior e menor peso como 0
maior = 0
menor = 0

# Cria uma estrutura for para gerar 6 pesos
for faixa in range(1, 6):
    peso = float(input(f'Digite o peso da {faixa} pessoa: '))

    # Ao digitar o primeiro valor em (faixa), o maior e menor valor é este, então lhe é atribuído
    if faixa == 1:
        maior = peso
        menor = peso

    # Depois, se o peso digitado for maior ou menor, este passa sê-lo, respectivamente
    else:
        if peso > maior:
            maior = peso
        if peso < menor:
            menor = peso

# Imprime o valor do maior e menor peso
print(f'O maior peso é {maior}Kg e o menor é {menor}Kg.')
