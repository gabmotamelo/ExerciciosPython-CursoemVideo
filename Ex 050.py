n=0
for i in range(1,7):
    x = int(input('Digite o {}° número: '.format(i)))
    if x%2==0:
        n=x+n

print('A soma dos números pares são: {}'.format(n))
