## Faça um programa que CALCULE o fatorial de um número, fornecido pelo usuário. Exemplo, cinco fatorial: 5! = 5*4*3*2*1

varGetNumber = int(input('Digite um número inteiro: '))
varFatorial = varGetNumber

while varGetNumber >= 2:
    varFatorial = varFatorial * (varGetNumber - 1)
    varGetNumber -= 1
print(varFatorial)

## Vamos fazer um programa que simule um cofre. Ele terá uma senha predefinida para acertar a senha. A cada tentativa errada o programa deverá mostrar a mensagem "Senha incorreta. Tente novamente". Se ele acertar a senha, o programa deverá mostrar a mensagem: "Senha correta."

varGetPass = int(input('Digite sua senha:'))

while varGetPass != 1511:
    print('Senha incorreta. Tente novamente')
    varGetPass = int(input('Digite sua senha:'))
print('Senha correta!')

## Faça um programa que simule um cofre. Ele terá uma senha predefinida e o usuário terá 3 tentativas para acertar a senha. A cada tentativa errada o programa deverá mostrar a mensagem 'Senha incooreta. Tente novamente.'. Quando a senha correta for digitada, o programa deverá retornar a mensagem 'Senha correta. Seja bem vindo.' 

senha = '0000'
tentativas = 3

while senha != 0:
    tentativa = input('Digite a senha de 4 dígitos: ')

    if tentativa == senha:
        print('A senha está correta.')
        break

    else:
        print('Senha incorreta. Tente outra vez.')
        tentativas -= 1
