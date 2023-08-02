# Leia o ano de nascimento do usuário e informe de acordo com sua idade:
# Se ainda vai se alistar; se está na hora de alistar; ou se já passou da hora.
# Também deve mostrar o tempo que falta ou que passou do prazo.

from datetime import date

print('[ 1 ] Masculino.')
print('[ 2 ] Feminino.')
sexo = int(input('Infome seu sexo: '))

if sexo == 1:
    ano = int(input('Ano de nascimento: '))

    ano_atual = date.today().year
    idade = ano_atual - ano
    excede = idade - 18
    faltam = 18 - idade

    print(f'Quem nasceu em {ano} completa {idade} anos em {ano_atual}.')

    if idade < 18:
        print(f'Ainda faltam {faltam} anos para seu alistamento.')
        print(f'Você deve se alistar em {ano_atual + faltam}.')
    elif idade == 18:
        print('Está na hora de se alistar! Corra e cumpra seu dever!')
    elif idade > 18:
        print(f'Já passou da hora de se alistar!')
        print(f'Passaram-se {excede} anos, você deveria ter se alistado em {ano_atual - excede}.')
if sexo == 2:
    print('Por ser do sexo feminino, você não precisa se alistar. Muito obrigado!')
