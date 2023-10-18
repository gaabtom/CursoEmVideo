'''Crie um programa onde o usuário digite uma expressão matemática qualquer que use parênteses.
Seu app deverá analisar se a expressão passada está com parênteses abertos e fechados na ordem correta.'''

expr = str(input('Digite uma expressão: '))
guarda_parenteses = []
for simbolo in expr:
    if simbolo == '(':
        guarda_parenteses.append('(')
    elif simbolo == ')':
        if len(guarda_parenteses) > 0:
            guarda_parenteses.pop()
        else:
            guarda_parenteses.append('(')
            break
if len(guarda_parenteses) == 0:
    print('A expressão digitada é válida!')
else:
    print('A expressão digitada está errada.')