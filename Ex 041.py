ano = int(input('Digite o ano de nascimento do ATLETA : '))
idade = 2021-ano
if idade<=9:
    print('ATLETA DA CATEGORIA MIRIM')
elif idade>9 and idade<=14:
    print('ATLETA DA CATEGORIA INFANTIL')
elif idade>14 and idade<=19:
    print('ATLETA DA CATEGORIA JUNIOR')
elif idade>19 and idade<=20:
    print('ATLETA DA CATEGORIA SÊNIOR')
elif idade>20:
    print('ATLETA DA CATEGORIA MASTER')
