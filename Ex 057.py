genero =  str(input('Digite o sexo da pessoa [M/F]: '))
while genero not in 'MFmf':
    print('Dados incorretos...Digite novamente! ')
    genero = str(input('Digite o sexo da pessoa [M/F]: '))
print('Registrado com sucesso!')

