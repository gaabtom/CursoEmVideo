# Calcule o valor a ser pego por um produto, considerando
# o preço normal e a condição de pagamento:
# À vista dinheiro/cheque: 10% desconto;
# À vista cartão: 5% desconto;
# Até 2x no cartão: preço normal;
# 3x ou mais no cartão: 20% juros.

print(f'{" LOJAS BARCELOS " :=^40}')

valor = float(input('Digite o valor das compras: R$'))

print('''FORMAS DE PAGAMENTO
[ 1 ] à vista dinheiro/cheque
[ 2 ] à vista cartão
[ 3 ] 2x no cartão
[ 4 ] 3x ou mais no cartão''')
pag = int(input('Qual opção deseja? '))

if pag == 1:
    print(f'Você terá um desconto de 10%, pagando apenas R${valor - (0.10 * valor):.2f}!')
elif pag == 2:
    print(f'Você terá um desconto de 5%, pagando apenas R${valor - (0.05 * valor):.2f}!')
elif pag == 3:
    print(f'Você pagará em 2x de R${valor / 2}')
    print(f'Pagando em 2x no cartão, você pagará os mesmo valor, de R${valor:.2f}.')
elif pag == 4:
    parcelas = int(input('Quantas parcelas? '))
    print(f'Você pagará em {parcelas}x de R${(valor + 0.20 * valor) / parcelas:.2f}.')
    print(f'Você contará com uma taxa de juros de 20%, pagando R${valor + (0.20 * valor):.2f}.')
else:
    print('Opcão INVÁLIDA de pagamento. Tente novamente.')
