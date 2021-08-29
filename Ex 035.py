a = float(input('Digite o comprimento da primeira reta: '))
b = float(input('Digite o comprimento da segunda reta: '))
c = float(input('Digite o comprimento da terceira reta: '))
if (a>b)and(a>c):
    maior = a
    menorA = b
    menorB = c
else:
    if (b>a)and(b>c):
        maior = b
        menorA = a
        menorB = c
    else:
        maior = c
        menorA = a
        menorB = b
menor = menorA+menorB
if (maior<menor):
    print('Pode formar um triângulo!')
else:
    print("Não pode formar um triângulo!")
