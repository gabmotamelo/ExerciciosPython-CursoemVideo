lista = [int(input('Digite o 1º número:')),
         int(input('Digite o 2º número:')),
         int(input('Digite o 3º número:')),
         int(input('Digite o 4º número:')),
         int(input('Digite o 5º número:'))]
print(f'Você digitou os valores {lista}')
if lista.count(max(lista))>1:
    print(f'O maior valor digitado foi {max(lista)} nas posições ',end='')
else:
    print(f'O maior valor digitado foi {max(lista)} na posição ', end='')
for i in range(0,5):
    if lista[i]==max(lista):
        print(f'{i}... ',end='')

print('\n')
if lista.count(min(lista))>1:
    print(f'O menor valor digitado foi {min(lista)} nas posições ',end='')
else:
    print(f'O menor valor digitado foi {min(lista)} na posição ', end='')
for x in range(0,5):
    if lista[x]==min(lista):
        print(f'{x}... ',end='')
