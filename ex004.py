x = input('Digite algo para ver seu tipo primitivo e informações:')
print('{} é do tipo {}!'.format(x, type(x))), print('{} é numérico? {}'.format(x, x.isnumeric())), \
    print('{} faz parte do alfabeto? {}'.format(x, x.isalpha())), \
    print('{} está em letras maiúsculas? {}'.format(x, x.isupper())), \
    print('{} é alfabético-númerico? {}'.format(x, x.isalnum())), \
    print('{} é caractere? {}'.format(x, x.isascii()))
