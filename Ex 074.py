from random import sample
num = tuple(sample(range(10),5))
print(f'Os valores sorteados foram: {num}')
print(f'''
O menor valor sorteado foi {min(num)}

O maior valor sorteado foi {max(num)}''')