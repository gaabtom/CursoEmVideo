# Inicializações das variáveis para armazenar informações sobre o programa
mulher_menosde20 = 0  # Contador para o número de mulheres com menos de 20 anos
nome_homem = ''  # Armazena o nome do homem mais velho
idade_homem = 0  # Armazena a idade do homem mais velho
idades = 0  # Armazena a soma das idades das pessoas

# Loop para ler informações sobre 4 pessoas
for pessoa in range(1, 5):
    print(f' ----- {pessoa}ª PESSOA ------')
    nome = str(input('Nome: ')).strip()  # Lê o nome da pessoa e remove espaços extras
    idade = int(input('Idade: '))  # Lê a idade da pessoa
    gen = str(input('Sexo [M/F]: ')).upper()  # Lê o sexo da pessoa e converte para maiúsculas

    idades += idade  # Acumula a idade para calcular a média mais tarde

    # Verifica se é a primeira pessoa lida e se é um homem para inicializar os dados do homem mais velho
    if pessoa == 1 and gen in 'Mm':
        nome_homem = nome
        idade_homem = idade

    # Verifica se a pessoa é um homem e se sua idade é maior do que a idade do homem mais velho atual
    if gen in 'Mm' and idade > idade_homem:
        nome_homem = nome
        idade_homem = idade

    # Verifica se a pessoa é uma mulher com menos de 20 anos
    if gen in 'Ff' and idade < 20:
        mulher_menosde20 += 1

# Calcula a média das idades e exibe os resultados finais
print(f'A média de idade do grupo é de {idades / 4} anos.')
print(f'O homem mais velho se chama {nome_homem}, e tem {idade_homem} anos.')
print(f'Ao todo são {mulher_menosde20} mulheres com menos de 20 anos.')
