print('='*30)
print('      BANCO MOTA')
print('='*30)
while True:
    valor = int(input('Que valor você quer sacar? R$'))
    notas50 = valor//50
    resto50 = valor-(notas50*50)
    if notas50==1:
        print('Total de {} cédula de R$50'.format(notas50))
    elif notas50>1:
        print('Total de {} cédulas de R$50'.format(notas50))
    notas20 = resto50//20
    resto20 = resto50 -(notas20*20)
    if notas20==1:
        print('Total de {} cédula de R$20 '.format(notas20))
    elif notas20>1:
        print('Total de {} cédulas de R$20 '.format(notas20))
    notas10 = resto20//10
    resto10 = resto20-(notas10*10)
    if notas10==1:
        print('Total de {} cédula de R$10'.format(notas10))
    elif notas10>1:
        print('Total de {} cédulas de R$10'.format(notas10))
    notas1 = resto10//1
    if notas1==1:
        print('Total de {} cédula de R$1'.format(notas1))
    elif notas1>1:
        print('Total de {} cédulas de R$1'.format(notas1))
    break
print('='*30)
print('Volte sempre ao BANCO MOTA! Tenha um bom dia!')

