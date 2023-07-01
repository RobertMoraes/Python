"""
Conjuntos

- Conjuntos em qualquer linguagem de programacao, estamos fazendo referencia a Teoria dos Conjuntos da Matematica.

- Em Python, os conjuntos sao chamados de Sets.
- Sets (conjuntos) nao possuem valores duplicados;
- Sets (conjuntos) nao possuem valores ordenados;
- Elementos nao sao acessados via indice, ou seja, conjuntos nao sao indexados;

Conjuntos sao bons para se utilizar quando precisamos armazenar elementos, mas nao nos importamos com a ordenacao deles. Quando nao precisamos se preocupar com chaves, valores e itens duplicados.

Os conjuntos (sets) sao referenciados em Python com chaves {}

Diferencao entre Conjuntos (Set) e Mapas (Dicionarios) em Python:
    - Um dicionario tem chaves/valor;
    - Um conjunto tem apenas valor;
"""
# Definindo um conjunto:

# Forma 1

s = set({1, 2, 3, 4, 5, 6, 7, 8, 9})  # Repare que temos valores repetidos.

print(s)
print(type(s))

# OBS: Ao criar um conjunto, caso seja adicionado um valor ja existente, o mesmo será ignorado sem gerar error e nao fara parte do conjunto.

# Forma 2 - Mais comum

s = {1, 2, 3, 4, 5, 6, 7, 8, 9}
print(s)
print(type(s))

if 3 in s:
    print('Tenho 3')
else:
    print('Não tenho 3')

dados = 99, 2, 35, 2, 4, 19, 99, 13, 35, 87, 1, 0, 53

lista = list(dados)
print(f'Lista: {lista} com {len(lista)}')
print(type(lista))

tupla = tuple(dados)
print(f'Tupla: {tupla} com {len(tupla)}')
print(type(tupla))

dicionario = {}.fromkeys(dados, 'dados')
print(f'Dict: {dicionario} com {len(dicionario)}')
print(type(dicionario))

conjunto = set(dados)
print(f'Conjunto: {conjunto} com {len(conjunto)}')
print(type(conjunto))

s = {1, 'b', True, 23.41, 5}
print(s)
print(type(s))
for valor in s:
    print(valor)

cidades = ['MG', 'SP', 'RJ', 'ES', 'RS', 'SP', 'MG', 'ES']
print(cidades)
print(type(cidades))
print(len(cidades))
print(len(set(cidades)))

estudantes_python = {'Robert', 'Pedro', 'Marcelo', 'Bruna', 'Patricia', 'Juliana', 'Gustavo', 'Bruno', 'Carlos', 'Pamela'}

estudantes_java = {'Robert', 'Bruna', 'Gustavo', 'Carlos', 'Katia', 'Vanessa'}

unicos1 = estudantes_python.union(estudantes_java)
print(len(unicos1))
print(unicos1)

unicos2 = estudantes_python | estudantes_java
print(len(unicos2))
print(unicos2)

ambos1 = estudantes_python.intersection(estudantes_java)
print(len(ambos1))
print(ambos1)

ambos2 = estudantes_python & estudantes_java
print(len(ambos2))
print(ambos2)

somente_python = estudantes_python.difference(estudantes_java)
print(f'Estudantes somente Python: {somente_python}')
somente_java = estudantes_java.difference(estudantes_python)
print(f'Estudantes somente Java: {somente_java}')
