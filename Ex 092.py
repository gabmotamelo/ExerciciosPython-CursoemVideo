dados = {'nome':str(input('Nome: ')),
         'idade':2021 - (int(input('Ano de nascimento: '))),
         'ctps':int(input('Carteira de Trabalho: (0 não tem): ')),
         'contratação':int(input('Ano de Contratação: ')),
         'salário':float(input('Salário: R$'))}
if dados['ctps']==0:
    dados['ctps'] = "não possui"
else:
    dados['aposentadoria']=(dados['contratação']-(2021-dados['idade'])+35)
print('=-'*30)
print(dados)
for k,v in dados.items():
    print(f'{k} tem o valor {v}.')
