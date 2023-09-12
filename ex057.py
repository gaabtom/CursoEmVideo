'''Faça um programa que leia o sexo de uma pessoa, mas só aceite os valores 'M' ou 'F'.
Caso esteja errado, peça a digitação novamente até ter um valor correto.'''
# Lê o sexo do usuário
sexo = str(input('Digite seu sexo: [M/F] ')).upper().strip()[0]

# Enquanto o sexo do usuário não estiver em 'MF', o sistema repete a pergunta
while sexo not in 'MF':
    sexo = str(input('Sexo inválido! Por favor, informe seu sexo: [M/F] ')).strip().upper()[0]

# Ao informar o sexo corretamente, mostra qual foi informado e encerra o programa
print(f'Sexo {sexo} registrado com sucesso.')