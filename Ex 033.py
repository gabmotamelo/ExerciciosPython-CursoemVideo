a = float(input('Digite o primeiro número: '))
b = float(input('Digite o segundo número: '))
c = float(input('Digite o terceiro número: '))
if (a>b)and(a>c)and(b>c):
    print('O primeiro número({}) é o maior! '.format(a))
    print('O terceiro número({}) é o menor!'.format(c))
else:
    if (a>b)and(a>c)and(c>b):
        print('O primeiro número({}) é o maior!'.format(a))
        print('O segundo número({}) é o menor!'.format(b))
    else:
        if (b>a)and(b>c)and(c>a):
            print('O segundo número({}) é o maior!'.format(b))
            print('O primeiro número({}) é o menor!'.format(a))
        else:
            if (b>a)and(b>c)and(a>c):
                print('O segundo número({}) é o maior!'.format(b))
                print('O terceiro número({}) é o menor!'.format(c))
            else:
                if (c>a)and(c>b)and(b>a):
                    print('O terceiro número({}) é o maior!'.format(c))
                    print('O primeiro número({}) é o menor!'.format(a))
                else:
                    print('O terceiro número({}) é o maior!'.format(c))
                    print('O segundo número({}) é o menor!'.format(b))
