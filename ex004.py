x = input('Digite algo para ver seu tipo primitivo e informações:')
print(f'É do tipo primitivo: {type(x)}')
print(f'É numérico? {x.isnumeric()}')
print(f'É alfabético? {x.isalpha()}')
print(f'Está em maiúsculas? {x.isupper()}')
print(f'Está em minúsculas? {x.islower()}')
print(f'É alfabético-númerico? {x.isalnum()}')
print(f'É captalizada? {x.istitle()}')
print(f'Só tem espaços? {x.isspace()}')

