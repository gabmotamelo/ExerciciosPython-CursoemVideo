nota2 = []
nota = []
nome = []
lista = [[nome],[nota],[nota2]]
while True:
    nome.append(str(input('Nome: ')))
    nota.append(float(input('Nota 1: ')))
    nota2.append(float(input('Nota 2: ')))
    decisao = str(input('Quer continuar? [S/N]')).strip().upper()[0]
    if decisao == 'N':
        break
print('-='*30)
print(f'{"No.":<4}{"NOME":<10}{"MÉDIA":>8}')
print('-'*30)
for i in range(0,len(nome)):
    media = (nota[i]+nota2[i])/2
    print(f'{i:<4}{nome[i]:<10}{media:>8.1f}')
print('-'*40)
while True:
    mostrar = int(input('Mostrar notas de qual aluno? (999 interrompe):'))
    if mostrar<len(nome) and mostrar!=999:
        print(f'Notas de {nome[mostrar]} são {nota[mostrar]}, {nota2[mostrar]} ')
        print('-' * 40)
    elif mostrar==999:
        print('FINALIZANDO...\n<<< VOLTE SEMPRE >>>')
        break
    else:
        print(f'No. inválido,digite novamente...')
        print('-' * 40)


