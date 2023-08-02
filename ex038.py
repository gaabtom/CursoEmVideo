# Leia dois números inteiros e compare-os, mostrando na tela uma mensagem:
# o primeiro valor é maior; o segundo valor é maior; os dois são iguais.

num1 = int(input('Digite um número inteiro: '))
num2 = int(input('Digite outro número: '))

if num1 > num2:
    print(f'O \033[1;31mPRIMEIRO\033[m número é \033[1;32mMAIOR\033[m!')
elif num2 > num1:
    print(f'O \033[1;31mSEGUNDO\033[m número é \033[1;32mMAIOR\033[m!')
else:
    print(f'Os números são \033[1;33mIGUAIS\033[m!')
