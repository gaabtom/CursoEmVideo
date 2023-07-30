# Programa que pergunte a distância de uma viagem e calcule o preço da passagem de ônibus,
# sendo que para viagens de até 200km é cobrado R$0,50 p/km, e acima disso, R$0,45.

# determina a distancia da viagem
distancia = float(input('Qual a distância, em Km, da viagem desejada? '))

# determina o preço por km a depender da distancia
ate_200km = 0.50
mais_de_200km = 0.45

# determina o valor de acordo com a distancia
if distancia <=200:
    print(f'O valor da sua passagem equivale a R${ate_200km} por Km, resultando no total de R${distancia * ate_200km:.2f}!')
else:
    print(f'O valor da sua passagem equivale a R${mais_de_200km} por Km, resultando no total de R${distancia * mais_de_200km:.2f}!')


