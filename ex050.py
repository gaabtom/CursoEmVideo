# Desenvolva um programa que leia seis números inteiros e mostre a soma apenas daqueles que
# forem pares. Se o valor digitado for ímpar, desconsidere-o.

# Determina o valor da soma e do contador
soma = 0
cont = 0

# Estrutura for que lê 6 números
for c in range(1, 7):
    n = int(input(f'Digite o {c} número: '))
    # Se o resto da divisão de n for igual a 0, adiciona o número digitado a soma, e +1 ao contador
    if n % 2 == 0:
        soma += n
        cont += 1
# Mostra na tela a quantidade de números pares contados e a soma dos mesmos
print(f'A soma dos {cont} valores PARES digitados é igual a {soma}!')
