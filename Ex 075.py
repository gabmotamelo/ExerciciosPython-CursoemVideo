x = int(input('Digite um número: '))
y = int(input('Digite outro número: '))
z = int(input('Digite outro número: '))
w = int(input('Digite outro número: '))
tupla = (x,y,z,w)
print(f'Você digitou os valores {tupla}')
if tupla.count(9)==1:
    print(f'O valor 9 apareceu {tupla.count(9)} vez')
else:
    print(f'O valor 9 apareceu {tupla.count(9)} vezes')
if 3 not in tupla:
    print(f'O valor 3 não aparece em nenhuma posição')
else:
    print(f'O valor 3 apareceu na {tupla.index(3)+1}ª posição')
print(f'Os valores pares digitados foram:',end='')
for i in tupla:
    if i%2==0:
        print(f'{i} ',end='')