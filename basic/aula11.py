# Laço For In

for dia in['Segunda', 'Terça', 'Quarta', 'Quinta', 'Sexta']:
    print(dia)

for numero in [0, 1,  2, 3, 4, 5]:
    print(numero, end = ' ')

for number in range(20):# o range vai retornar do zero ao 19, portanto 20 números
    print(number, end = ' ')

# Digamos que seja necessário mostrar os números de 5 ao 10
for sequence in range(5,11):
    print(sequence)

# Para começar no 5 e ir até o 55, contando de 5 em 5, add o número 5 ao último parâmetro
for seq5 in range(5,56,5):
    print(seq5, end = ' ')