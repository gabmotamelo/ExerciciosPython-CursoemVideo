x = int(input('Digite um número:'))
tot = 0
for i in range(1,x+1):
    if x%i==0:
        print('\033[33m',end='')
        tot += 1
    else:
        print('\033[31m', end='')
    print('{} '.format(i), end='')
print('\n\033[mO número {} foi divisível {} vezes'.format(x,tot))
if tot == 2:
    print('E por isso ele é PRIMO! ')
else:
    print('E por isso ele NÃO É PRIMO!')

