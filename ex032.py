# Leia se um ano qualquer é bissexto ou não.

# importa da biblioteca datetime a função date que informa a data
from datetime import date

# determina o ano a ser analisado
ano = int(input('Digite um ano, se quiser analisar o ano atual, digite 0: '))

# determina se o ano atual é bissexto ou não
if ano == 0:
    ano = date.today().year

# se o ano for divisível por 4 e não por 100, ou por 4, 100 e 400, será bissexto
if (ano % 4)== 0 and (ano % 100)!= 0 or (ano % 4)==0 and (ano % 100)==0 and (ano % 400)== 0:
    print(f'0 ano de {ano} é bissexto! Que legal!')

# mostra a mensagem a seguir se não for bissexto
else:
    print(f'O ano de {ano} não é bissexto. Meh.')
    