# Exercícios If

# 1- Faça um programa que recebe do usuário duas notas de zero a dez e escreva na tela "Você está aprovado. Parabéns!", caso a média das duas notas seja maior ou igual a sete.

varGetGrade1 = eval(input('Digite a primeira nota'))
varGetGrade2 = eval(input('Digite a segunda nota'))

if (varGetGrade1 + varGetGrade2) / 2 >= 7:
    print('Você está aprovado. Parabéns!')

# 2- Faça um programa que recebe do usuário duas notas de zero a dez e escreva na tela "Você está aprovado. Parabéns!", caso a média das duas notas seja maior ou igual a sete. Caso não seja maior que sete, o programa deve escrever na tela "Você foi reprovado."

varGetGrade1 = eval(input('Digite a primeira nota'))
varGetGrade2 = eval(input('Digite a segunda nota'))

if (varGetGrade1 + varGetGrade2) / 2 >= 7:
    print('Você está aprovado. Parabéns!')
else:
    print('Você foi reprovado.')

# 3- Usando os exercícios anteriores como base, acrescente uma terceira condição, se caso a média for maior ou igual a cinco e menor que sete, escreva na tela "Você está de recuperação final."

varGetGrade1 = eval(input('Digite a primeira nota'))
varGetGrade2 = eval(input('Digite a segunda nota'))
varMedia = (varGetGrade1 + varGetGrade2) / 2

if varMedia >= 7:
    print('Você está aprovado. Parabéns! Sua média foi : ', varMedia)
elif varMedia >= 5 and varMedia < 7:
    print('Você está de recuperação final. Sua média atual é : ', varMedia)
else:
    print('Você foi reprovado. Sua média foi : ', varMedia)
    