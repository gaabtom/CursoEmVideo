# Leia duas notas de um aluno e apresente, a partir da média atingida:
# Abaixo de 5: reprovado;
# Entre 5 e 6.9: recuperação;
# Média 7 ou superior: aprovado.

from time import sleep

print('\033[35m-='*20)
print('\033[36mAnalisador de Notas')
print('\033[35m-=\033[m'*20)

nota1 = float(input('Digite sua primeira nota: '))
nota2 = float(input('Digite sua segunda nota: '))
media = (nota1 + nota2) / 2

print(f'Sua média foi \033[1;33m{media}\033[m!')
print('\033[4;34mPortanto...\033[m')
sleep(1)

if media <5:
    print('Você foi \033[1;31mREPROVADO\033[m! Estude mais.')
elif media == 5 or media < 7:
    print('Você está de \033[1;33mRECUPERAÇÃO\033[m! Que pena.')
elif media >= 7:
    print('Você foi \033[1;32mAPROVADO\033[m! Parabéns!')

print('\033[1;31m[FIM]')


