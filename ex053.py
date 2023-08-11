''' Crie um programa que leia uma frase e diga se ela é um palíndromo, desconsiderando espaços e acentos.
 Ex: Apos a Sopa
 A sacada da casa
 A torre da derrota
 O lobo ama o bolo
 Anotaram a data da maratona '''

# Solicita ao usuário que digite uma frase, dividindo-a e colocando-a em maiúsculo
frase = str(input('Digite uma frase: ')).strip().upper()

# Divide a frase em palavras (.split) e as junta sem espaços (''.join)
palavras = frase.split()
junto = ''.join(palavras)

# Inicializa uma variável para armazenar a versão inversa da frase ('') - vazio
inverso = ''

''' Utiliza da estrutura for para gerar a frase de trás para frente, 
lê a quantidade de caracteres de junto -1 (início), e vai até o final (-1), voltando de 1 em 1 (-1) '''
for letra in range(len(junto) - 1, -1, -1):
    inverso += junto[letra]

# Imprime a frase invertida
print(f'O inverso de {junto} é {inverso}.')

# Verifica se a frase invertida é igual à frase original, determinando se é um palíndromo
if inverso == junto:
    print('Temos um palíndromo!')
else:
    print('A frase digitada não é um palíndromo.')
