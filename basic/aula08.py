# Condicional If

# Construa um programa que verifica se a temperatura digitada pelo usuário é quente ou fria

varGetTemp = eval(input('Digite a temperatura'))

if varGetTemp >= 32:
    print('Está muito calor!')
elif varGetTemp <= 31 and varGetTemp >= 22:
    print('A temperatura está agradável')
else:
    print('Está frio!')
    