"""
Loop for

Loop -> Estrutura de repetição
For -> Uma dessas estruturas

C ou Java

for(int i = 0; i < 10; i++){
    //execução do loop
}

Python

for item in interavel:
    //execucao do loop

Utilizamos loops para iterar sobre sequencias ou sobre valores iteraveis

Exemplos de iteraveis:
- String
    nome = 'Robert'
- Lista
    lista = [1,2,3,4,5]
- Range
    numeros = range(1,10)

"""

nome = 'Robert'
lista = [1, 2, 3, 4, 5]
numeros = range(1, 10)  # Temos que transformar em uma lista

print('CASE 1 ::::::::::::::::::::::::::::::')
# Exemplo de for (Iterando sobre uma string)
for letra in nome:
    print(letra)

print('CASE 2 ::::::::::::::::::::::::::::::')
# Exemplo de for (Iterando sobre uma lista)
for numero in lista:
    print(numero)

print('CASE 3 ::::::::::::::::::::::::::::::')
# Exemplo de for (Iterando sobre uma range)
"""
range(valor_inicial, valor_final)
OBS: O valor final é inclusive.
1
2
3
4
5
6
7
8
9
10 - Não inclui
"""
for numero in range(1, 10):
    print(numero)

print('CASE 4 ::::::::::::::::::::::::::::::')
for i, v in enumerate(nome):
    print(i, v)

print('CASE 5 ::::::::::::::::::::::::::::::')
# Quando não precisamos de um valor, podemos descartá-lo utilizando um underline(_)
for _, v in enumerate(nome):
    print(v)

print('CASE 6 ::::::::::::::::::::::::::::::')
for valor in enumerate(nome):
    print(valor)

print('CASE 7 ::::::::::::::::::::::::::::::')
qtd = int(input('Quantas vezes esse loop de rodar? '))
soma = 0

for n in range(1, qtd + 1):
    num = int(input(f'Informe o {n}/{qtd} valor: '))
    soma = soma + num
print(f'A soma é {soma}')

print('CASE 8 ::::::::::::::::::::::::::::::')
# Exemplo de for (Iterando sobre uma string)
for letra in nome:
    print(letra, end=' ')

print('CASE 9 ::::::::::::::::::::::::::::::')
# Original: U+1F6AD
# Modificado: U0001F6AD
emoji = 'U0001F6AD'
for _ in range(3):
    for num in range(1, 11):
        print('\U0001F6AD' * num)
