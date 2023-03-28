# Desafio 024 - Crie um programa que leia uma cidade e diga se ela começa ou não com "SANTO".

cidade = input('Digite o nome de uma cidade: ').strip()
dividido = cidade.upper().split()
print('A cidade começa com "SANTO"?', 'SANTO' in dividido[0])





