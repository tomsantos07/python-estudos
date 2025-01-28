# Exercícios

# 1- Calcule a soma dos numeros do 10 ao 14
print('exercicio 1')
varSomaNumeros = sum([10,11,12,13,14])
print(varSomaNumeros)

# 2- Calcule a média entre os números 10,15,20
# Nesse caso, pesquisei pela função que retorna o número de itens de um array e utilizei para que o cálculo de média ficasse dinâmico
print('exercicio 2')
varNumeros = [10, 15, 20]
varSoma = sum(varNumeros)
varMedia = varSoma / len(varNumeros)
print(varMedia)

# 3- Peça para o user digitar duas notas de zero a dez e os pesos das notas e calcule a média ponderada entre elas. Exemplo: media = (nota1 + nota2 * peso2) / (peso1 + peso2). Lembrando que a soma dos pesos precisa ser 10.
print('exercicio 3')
nota1 = input('Digite a primeira nota')
nota1 = eval(nota1)
nota2 = input('Digite a segunda nota')
nota2 = eval(nota2)
peso1 = input('Digite o peso da primeira nota')
peso1 = eval(peso1)
peso2 = input('Digite o peso da segunda nota')
peso2 = eval(peso2)

varSomaNota = sum([nota1, nota2])
varSomaPeso = sum([peso1, peso2])

varNumerador = varSomaNota * peso2
varResult = varNumerador / varSomaPeso

print(varResult)

# 4- Qual o menor preço dessa lista?
# preços: R$100.20, R$34.90, R$18.95
print('exercicio 4')
varPrecos = [100.20, 34.90, 18.95]
varMenorPreco = min(varPrecos)
print(varMenorPreco)


