"""
Listas

Listas em Python funcional como vetores/matrizes (arrays) em outras linguagens, com a diferenca de serem DINAMICO e tambem podemos colocar QUALQUER tipo de dado.

Linguagens C/JAVA: Arrays
    - Possuem tamanho e tipo de dado fixo;
    Ou seja, nestas linguagens se voce criar um array do tipo int e com tamanho 5, este array será SEMPRE do tipo inteiro e podera ter SEMPRE no maximo 5 valores.

Liguagem Python:
    - Dinamico: Nao possui tamanho fixo;
    Ou seja, podemos criar a lista e simplesmente ir adicionando elementos;
    - Qualquer tipo de dado: Nao possuem tipo de dado fixo;
    Ou seja, podemos colocar qualquer tipo de dado;

As listas em Python sao representadas por colchetes: []
"""
# type([])
#
# nome = 'robert'  # input('Informe seu nome completo: ')
#
# lista1 = [1, 99, 4, 27, 147, 43, 19, 80]
#
# lista2 = ['r', 'o', 'b', 'e', 'r', 't']
#
# lista3 = list('Robert Moraes')
#
# lista4 = list(range(11))
#
# lista5 = list(nome.lower())
#
# if 27 in lista1:
#     print('Numero encontrado!')
# else:
#     print('Numero solicitado não existe!')
#
# for letra in lista5:
#     print(letra, end='')
#
# # Podemos facilmente ordenar uma lista
# print('::::::::::::::: ORDERNAR LISTA :::::::::::::::::::')
# print('::::::::::::::: LISTA 1 :::::::::::::::::::')
# print(lista1)
# lista1.sort()
# print(lista1)
# print('::::::::::::::: LISTA 5 :::::::::::::::::::')
# print(lista5)
# lista5.sort()
# print(lista5)
#
# # Podemos facilmente contar o numero de ocorrencia de uma valor em uma lista
# print('::::::::::::::: CONTA NUMERO DE OCORRENCIA :::::::::::::::::::')
# print(lista1.count(1))
# print(lista5.count('e'))

# Adicionar elementos em listas

"""
Para adicionar elementos em listas, utilizamos a função append

OBS: Com append, nós só conseguimos adicionar 1 elemento por vez. Com extend podemos adicionar 2 elementos ou mais dentro de uma lista existente 
"""
# print('::::::::::::::: LISTA 1 :::::::::::::::::::')
# print(lista1)
# lista1.append(27)
# lista1.sort()
# print(lista1)
# lista1.extend([78, 98, 123])
# print(lista1)
#
# # Podemos inserir um novo elemento na lista informando a posição do indice
# # OBS: Isso nao substitui o valor inicial. O mesmo sera deslocado para direita da lista
# print(lista1)
# lista1.insert(4, 'Novo Valor')
# print(lista1)
# lista1.remove('Novo Valor')
#
# # Podemos facilmente juntar duas listas
#
# lista6 = lista1 + lista5
# print(lista6)
# lista6.reverse()
# print(lista6)
# # lista6.sort() não é possível utilizar sort() em lista que contenha int e string
# lista1.sort()
# print(lista1)
# lista5.sort()
# print(lista5)
# lista6 = lista1 + lista5
# print(lista6)
#
# print(lista1[::-1])  # mesma coisa que o reverse
# print(lista5[::-1])  # mesma coisa que o reverse
#
# print(len(lista6))  # contar quanto elementos tem na lista
#
# # o pop remove o ultimo elemento e o retorna
# # obs: caso não tenha o indice na posição informado retorna IndexError
# print(lista6)
# a = lista6.pop()
# print(lista6)
# print(a)
# b = lista6.pop(3)
# print(lista6)
# print(b)
# lista7 = lista6
# print(lista7)
# print(lista7.clear())
#
# # convertendo string em lista
#
# # exemplo 1 - usando split() que por padrão separa os elementos da lista pelo espaço entre eles.
# curso = 'Python Fundamental'
# print(curso)
# curso = curso.split()
# print(curso)
#
# # exemplo 2 - especificando o separador
# curso = 'Programação,em,python'
# print(curso)
# curso = curso.split(',')
# print(curso)
#
# # convertendo uma lista em uma string
# lista7 = ['programação', 'em', 'python', 'essencial']
# print(lista7)
# # colocando como separador espaço
# curso = ' '.join(lista7)
# print(curso)
# # colocando como separador $
# curso = '$'.join(lista7)
# print(curso)

# Iterando sobre listas

# print(':::::::::: LISTA DE TABUADA::::::::::')
# # exemplo 1 - tabuada
# listaTabuada = list(range(11))
# resultTabuada = []
# print(listaTabuada)
# tabuada = int(input("Informe o numero da tabuada: "))
# for elemento in listaTabuada:
#     resultTabuada.append(listaTabuada[elemento] * tabuada)
#     print(f'{listaTabuada[elemento]} * {tabuada} = {resultTabuada[elemento]}')
#
# print(resultTabuada)
# print(resultTabuada.index(8))
#
# print(':::::::::: LISTA DE COMPRAS ::::::::::')
# carrinho = []
# produto = ''
# resposta = ''
#
# while produto != 'sair':
#     print("Adicione um produto na lista ou digite 'sair' para finalizar: ")
#     produto = input()
#     if produto != 'sair':
#         carrinho.append(produto)
#     else:
#         print("Deseja remover algum produto? Digite 'sim' para remover ou 'não' para continuar: ")
#         resposta = input()
#         if resposta == 'sim':
#             print("Informe o nome do produto: ")
#             produto = input().lower()
#             # validaProduto = carrinho.count(produto)
#             indiceProduto = carrinho.index(produto)
#             if indiceProduto > 0:
#                 # carrinho.remove(produto)
#                 carrinho.pop(indiceProduto)
#             else:
#                 print("Produto não encontrado.")
#
# print(':::::::: UTILIZANDO WHILE ::::::::')
# indice = 0
# while indice < len(carrinho):
#     print(indice, carrinho[indice])
#     indice += 1
#
# print(':::::::: UTILIZANDO FOR ::::::::')
# for ind, produto in enumerate(carrinho):
#     print(ind, produto)

print(':::::::::: REVISAO DE SLICING ::::::::::')
# revisao de slicing
# lista[inicio:fim:passo]
# range(inicio:fim:passo)
# trabalhando com slice de lista com o parametro 'inicio'

listaSlice = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
listaSlice = list(range(1001))
print(listaSlice)
print(listaSlice[::9])  # iniciando no indice 1 e pegando todos os elementos restantes

print(':::::::::: SOMA, VALOR MAXIMO, VALOR MINIMO, TAMANHO ::::::::::')

listaValores = [1, 2, 3, 4, 5, 6]

print(sum(listaValores))  # soma
print(max(listaValores))  # maximo valor
print(min(listaValores))  # minimo valor
print(len(listaValores))  # tamanho da lista

print(':::::::::: TRANSFORMAR LISTA EM TUPLA ::::::::::')

print(listaValores)
print(type(listaValores))

tupla = tuple(listaValores)
print(tupla)
print(type(tupla))

print(':::::::::: DESEMPACOTAMENTO DE LISTAS ::::::::::')
# Obs: Para desempacotamento precisa ter o mesmo numero de variaveis criadas para o numero de elementos na lista, caso contrario ocorrerá ValueError
num1, num2, num3, num4, num5, num6 = listaValores

print(num1)
print(num2)
print(num3)

print(':::::::::: COPIANDO LISTA (SHALLOW COPY E DEEP COPY ::::::::::')

# Forma 1 - utilizando .copy() ele criara lista independentes, isso é chamado de Deep Copy
print(listaValores)
nova = listaValores.copy()
print(nova)
nova.append(7)
print(listaValores)
print(nova)

# Forma 2 - utilizando copia via atribuicao isso faz como que qualquer alteracao em uma das listas reflita na outra, isso é chamado de Shallow Copy

print(listaValores)
nova = listaValores
print(nova)
nova.append(7)
print(listaValores)
print(nova)
