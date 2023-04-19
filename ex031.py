# Programa que pergunte a distância de uma viagem e calcule o preço da passagem de ônibus,
# sendo que para viagens de até 200km é cobrado R$0,50 p/km, e acima disso, R$0,45.

distancia = float(input('Qual a distância em km de sua viagem? '))
duzentos_km = distancia * 0.50
mais_km = distancia * 0.45
if distancia <=200:
    print(f'Você pagará R${duzentos_km:.2f} por sua viagem. São cobrados R$0,50 por km.')
else:
    print(f'Você pagará R${mais_km:.2f} por sua viagem. São cobrados R$0,45 por km.')

