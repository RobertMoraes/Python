"""
Tuplas (tuple)

Tuplas são parecidas com listas.

Existem duas diferenças básicas:

1 - As tuplas são representadas por parênteses ()

2 - As tuplas são imutáveis: Isso significa que ao criar uma tupla ela não muda. Toda operação em uma tupla gera uma nova tupla.

"""
import random

# CUIDADO 1: As tuplas são representadas por (), mas veja:
print(':::::::::: TUPLA - 1 ::::::::::')
tupla1 = (1, 2, 3, 4, 5, 6)
print(tupla1)
print(type(tupla1))

print(':::::::::: TUPLA - 2 ::::::::::')
tupla2 = 1, 2, 3, 4, 5, 6
print(tupla2)
print(type(tupla2))

# CUIDADO 2: Tuplas com 1 elemento
print(':::::::::: TUPLA - 3 ::::::::::')
tupla3 = (4)  # Isso não é uma tupla
print(tupla3)
print(type(tupla3))

print(':::::::::: TUPLA - 4 ::::::::::')
tupla4 = (4,)  # Isso é uma tupla
print(tupla4)
print(type(tupla4))

print(':::::::::: TUPLA - 5 ::::::::::')
tupla5 = 4,  # Isso é uma tupla
print(tupla5)
print(type(tupla5))

# CONCLUSÃO: Podemos concluir que tuplas são definidas pela virgula e não pelo uso do parenteses

print(':::::::::: TUPLA - 6 ::::::::::')
tupla6 = tuple(range(0, 21, 2))
print(tupla6)
print(type(tupla6))

print(':::::::::: TUPLA - 7 ::::::::::')
tupla7 = ('Robert', 'Moraes')
nome, sobrenome = tupla7
print(nome)
print(sobrenome)

print(':::::::::: TUPLA - 8 ::::::::::')
# Metodos para adicao e remocao de elementos nas tuplas não existem, dado o fato que tuplas sao imutaveis.
# Soma, valor maximo, valor minimo e tamanho
# Se os valores forem todos inteiros ou reais

tupla8 = tuple(range(0, 101, random.randint(13, 33)))
print(tupla8)
print(sum(tupla8))
print(max(tupla8))
print(min(tupla8))
print(len(tupla8))

print(':::::::::: TUPLA - 9 ::::::::::')
# Concatenacao de tuplas

tupla9 = tuple(range(0, 101, random.randint(13, 33)))
print(tupla9)
tupla10 = tuple(range(0, 101, random.randint(13, 33)))
print(tupla10)

print(tupla9 + tupla10)

print(':::::::::: TUPLA - 10 ::::::::::')
# Gerando tupla de numeros aleatorios para jogo de adivinhação.
tupla11 = tuple(range(0, random.randint(0, 16539), random.randint(0, 163)))
print(tupla11)
# sorteado = int(input('Informe o numero da sorte: '))
# sorteio = False
sorteio = True
while not sorteio:
    status = sorteado in tupla11
    if not status:
        sorteado = int(input('Informe outro numero da sorte: '))
    else:
        sorteio = True
        print('Numero sorteado!')

print(':::::::::: TUPLA - 11 ::::::::::')
tupla12 = (1, 2, 3)

for n in tupla12:
    print(n)

for indice, valor in enumerate(tupla12):
    print(indice, valor)

print(':::::::::: TUPLA - 12 ::::::::::')
tupla12 = (1, 2, 3, 4, 5, 1, 6, 3, 4, 8, 9, 7, 9)
print(tupla12.count(1))

escola = tuple('Python Udemy')
print(escola)

print(escola.count('y'))

# a utilização de tupla é adequada SEMPRE que não houver necessidade de modificação dos dados contidos em uma coleção

# Exemplo 1
meses = ('Janeiro', 'Feveiro', 'Março', 'Abril', 'Maio', 'Junho', 'Julho', 'Agosto', 'Setembro', 'Outubro', 'Novembro', 'Dezembro')

print(meses)

for indice, valor in enumerate(meses):
    print(indice+1, valor)
i = 0
while i < len(meses):
    print(f'{i+1}|{meses[i]}')
    i += 1

print(meses[::2])

# Por que utilizar tuplas?

# - Tuplas são mais rápidas do que listas;
# - Tuplas deixam o código mais seguro;
# * Isso porque trabalhar com elementos imutáveis traz maior segurança para o código

