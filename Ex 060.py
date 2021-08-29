number = int(input('Digite um número para calcular seu fatorial: '))

result = 1
counter = 1

print('\nCalculando {}! = ' .format(number), end='')

while counter <= number:
    factorial = (number + 1) - counter
    if factorial > 1:
        print('{} x '.format(factorial), end='')
    result *= counter
    counter += 1
    if factorial == 1:
        print('1 = {}' .format(result))