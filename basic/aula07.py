# Exercicios Pt 2

# 5- Avalie se o número digitado pelo usuário é par ou ímpar. Se for par a saída deve mostrar True, se ímpar, deverá mostrar False.

varGetNumber = input('Digite um número:')
varGetNumber = eval(varGetNumber)

print(varGetNumber % 2 == 0)

# 6- Verifique se o menor preço dessa lista é menor que R$20.00
# preços: R$100.20, R$34.90, R$31.50, R$18.95

varPrecoMin = min([100.20, 34.90, 31.50, 18.95])
varParam = 20

print(varPrecoMin < varParam)

# 7 Faça um programa que converta temperatura em graus Fahrenheit fornecida pelo usuário em graus Celsius.
# celsius = (5/9) * (fahrenheit - 32)

varGetTemp = input('Digite a temperatura em graus Fahrenheit')
varGetTemp = eval(varGetTemp)
celsius = (5/9) * (varGetTemp - 32)
print(varGetTemp, 'é equivalente a ', celsius)