pessoal = list()
pessoa =dict()
soma = 0
while True:
    pessoa.clear()
    pessoa['Nome']=str(input("Nome: "))
    while True:
        pessoa['Sexo']=str(input("Sexo: [M/F] ")).strip().upper()[0]
        if pessoa['Sexo'] in 'MF':
            break
        print('Erro,digite novamente...')
    pessoa['Idade']=int(input("Idade: "))
    soma += pessoa['Idade']
    pessoal.append(pessoa.copy())

    while True:
        resp = str(input('Quer continuar? [S/N]')).upper().strip()[0]
        if resp in 'SN':
            break
        print('Digite S p/ sim ou N p/ não...')
    if resp=='N':
        break
print('-='*30)

if len(pessoal)==1:
    print(f'O grupo tem {len(pessoal)} pessoa.')
else:
    print(f'O grupo tem {len(pessoal)} pessoas.')
media = soma/len(pessoal)
print(f'A média de idade é de {media:.2f} anos.')
for i in pessoal:
    if i['Sexo']=="F":
        print(f'As mulheres cadastradas foram: {i["Nome"]} ',end='')
print()
print(f'Lista das pessoas que estão acima da média:')
for i in pessoal:
    if i['Idade']>=media:
        for k,v in i.items():
            print(f'{k} = {v};',end=' ')


