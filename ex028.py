# Faça o computador pensar em um número entre 0 e 5, e se o usuário acertar o número ele dirá que venceu, ou perdeu se errou.
import random
lista = [0, 1, 2, 3, 4, 5]
numero_maquina = random.choice(lista)
numero_usuario = int(input('Estou pensando em um número... Consegue adivinhar qual?'))
if numero_usuario == numero_maquina:
    print(f'Parabéns! Você ganhou! O número que pensei foi {numero_maquina}! ;)')
else:
    print(f'Féeum, féum féeumm... Você perdeu! O número que pensei foi {numero_maquina}! :p')
