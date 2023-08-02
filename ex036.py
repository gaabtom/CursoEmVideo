# Escreva um program a para aprovar o empréstimo bancário para a compra de uma casa.
# O programa vai perguntar: o valor da casa ; o salário ; e em quantos anos vai pagar.
# Calcule o valor da prestação mensal, sabendo que ela não pode execeder 30%
# do salário, ou o emrpréstimo será negado.

valor_casa = float(input('Digite o valor da casa: R$'))
salario = float(input('Digite seu salário: R$'))
anos_financiamento = int(input('Em quantos anos você quer financiar? '))
prestação = valor_casa / (anos_financiamento * 12)

print(f'Para pagar uma casa de R${valor_casa:.2f}, a prestação será de R${prestação:.2f}.')

if prestação > 30/100 * salario:
    print('O empréstimo foi \033[1;31mNEGADO\033[m! A prestação ultrapassa 30% de seu salário.')
elif prestação <= 30/100 * salario:
    print('Empréstimo \033[1;32mCONCEDIDO\033[m! Parabéns!')
