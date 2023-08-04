# Leia o ano de nascimento de um atleta e mostre sua categoria:
# Até 9 anos: mirim; Até 14 anos: infantil; Até 19 anos: junior;
# Até 20 anos: Sênior; Acima: Master.

from datetime import date

nasc = int(input('Digite seu ano de nascimento: '))
atual = date.today().year
idade = atual - nasc

print(f'Sua idade é de {idade} anos.')

if idade <= 9:
    print('Você é um atleta MIRIM!')
elif idade <= 14:
    print('Você é um atleta INFANTIL!')
elif idade <= 19:
    print('Você é um atleta JÚNIOR!')
elif idade <=25:
    print('Você é um atleta SÊNIOR!')
else:
    print('Você é um atleta MASTER! Uau!')
