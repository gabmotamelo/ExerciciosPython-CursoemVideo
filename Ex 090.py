nome = str(input('Nome: ')).upper()
media = float(input(f'Média de {nome}: '))
if media>=7:
    situacao = 'Aprovado'
else:
    situacao = 'Reprovado'
pessoa = {'name': nome, 'medium' : media,'situação':situacao}
print(f'Nome é igual a {pessoa["name"]}\nMédia é igual a {pessoa["medium"]}\nSituação é igual a {pessoa["situação"]} ')