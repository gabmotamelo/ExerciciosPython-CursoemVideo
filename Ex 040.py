nota1 = float(input('Digite a nota 1 do aluno: '))
nota2 = float(input('Digite a nota 2 do aluno: '))
media = (nota1+nota2)/2
if media<5.0:
    print('MEDIA = {:.1f}'.format(media))
    print('FOI REPROVADO!')
elif media>=5 and media<=6.9:
    print('MEDIA = {:.1f}'.format(media))
    print('RECUPERAÇÃO!')
elif media>=7.0:
    print('MEDIA = {:.1f}'.format(media))
    print('FOI APROVADO!')
    