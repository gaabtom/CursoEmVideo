# Faça o computador pensar em um número entre 0 e 5, e se o usuário acertar o número ele dirá que venceu, ou perdeu se errou.

# importando da biblioteca random a função randint, que gera um número inteiro entre (intervalo)
from random import randint

# importando da biblioteca time a função sleep, que faz o computador aguardar (segundos)
from time import sleep

# determinando número da máquina
número_máquina = randint(0, 5)

# mensagem para o usuário
print('-=-' * 20)
print('Estou pensando em um número entre 0 e 5. Tente adivinhar...')
print('-=-' * 20)

# determinando número do jogador
número_jogador= int(input('Em que número eu pensei? '))

# simulação de processamento com a função sleep (2 segundos)
print('Processando...')
sleep(2)

# condições de genhar ou perder
if número_jogador == número_máquina:
    print(f'Parabéns, você ganhou! O número que pensei foi de fato {número_máquina}! ;)')
else:
    print(f'Que azar! Você perdeu, o número que eu pensei foi {número_máquina}! Mais sorte da próxima vez! :p')
