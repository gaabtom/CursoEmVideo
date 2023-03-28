# Desafio 026 - Faça um programa que leia uma frase e mostre:
# Quantas vezes aparece a letra "A";
# Em que posição aparece pela primeira vez;
# Em que posição aparece pela última vez.

# Forma que eu fiz:
frase = input('Digite uma frase: ').strip()
dividido = frase.upper().split()
junto = ''.join(dividido)
quantidade = junto.count('A')
posição1 = junto.find('A')+1
posição2 = junto.rfind('A')+1
print('Nesta frase, o caractere "A":')
print(f'Aparece {quantidade} vezes.\nAparece pela primeira vez na posição {posição1}\nAparece pela última vez na posição {posição2}.')

# Forma apresentada no vídeo (adaptada por mim):

#frase = input('Digite uma frase: ').upper().strip()
#print('Nesta frase, o caractere "A":')
#print(f'Aparece {frase.count("A")} vezes.\nAparece pela primeira vez na posição {frase.find("A")+1}.\nAparece pela última vez na posição {frase.rfind("A")+1}.')

# OBS: a minha forma possibilita a contagem de posições sem contar qualquer espaço ENTRE as palavras, e a do vídeo não.