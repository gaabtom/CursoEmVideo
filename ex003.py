print('Insira os \033[1;33mnúmeros\033[m para \033[1;32msoma:\033[m ')
n1 = int(input('\033[4mPrimeiro Número:\033[m '))
n2 = int(input('\033[4mSegundo Número:\033[m '))
s = n1+n2
print('A soma entre \033[4;31m{}\033[m e \033[4;31m{}\033[m vale \033[4;32m{}\033[m!'.format(n1, n2, s))
