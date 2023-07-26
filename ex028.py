# Faça o computador pensar em um número entre 0 e 5, e se o usuário acertar o número ele dirá que venceu, ou perdeu se errou.
import random
lista = [0, 1, 2, 3, 4, 5]
número_máquina = random.choice(lista)
número_jogador= int(input('Estou pensando em um número entre 0 e 5, consegue adivinhar qual? '))
if número_jogador == número_máquina:
    print(f'Parabéns, você ganhou! O número que pensei foi de fato {número_máquina}! ;)')
else:
    print(f'Que azar! Você perdeu, o número que eu pensei foi {número_máquina}! Mais sorte da próxima vez! :p')
