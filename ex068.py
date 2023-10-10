from random import randint
num_vitoria = 0
print('-=' * 20)
print('PAR OU ÍMPAR?')
while True:
    print('-=' * 20)
    num_jogador = int(input('Digite um valor: '))
    parimpar = str(input('Par ou ímpar? [P/I] ')).upper().strip()[0]
    if parimpar not in 'PpIi':
        print('Jogada inválida! Tente novamente.')
        break
    num_maq = randint(1, 10)
    soma = num_jogador + num_maq
    print('-' * 30)
    print(f'Você jogou {num_jogador} e o computador {num_maq}. Total {soma}', end='')
    if soma % 2 == 0:
        print(' DEU PAR.')
        print('-' * 30)
        if parimpar in 'Pp':
            print('Você VENCEU!')
            print('Vamos jogar novamente...')
            num_vitoria += 1
        else:
            print('Você PERDEU!')
            if num_vitoria != 0:
                print('-=' * 20)
                print(f'GAME OVER! Você venceu {num_vitoria} vezes.')
            break
    elif soma % 2 != 0:
        print(' DEU ÍMPAR.')
        print('-' * 30)
        if parimpar in 'Ii':
            print('Você VENCEU!')
            print('Vamos jogar novamente...')
            num_vitoria += 1
        else:
            print('Você PERDEU!')
            if num_vitoria != 0:
                print('-=' * 20)
                print(f'GAME OVER! Você venceu {num_vitoria} vezes.')
            break
