"""
Modulo Collections - Counter (Contador)

Collections -> High-Performance Container Datetypes

Counter -> Recebe um interavel como parametro e cria um objeto do tipo Collections Counter que é parecido com um dicionario, contendo como chave o elemento da lista passada como paramentro e como valor a quantidade de ocorrencias desse elemento.
"""
from collections import Counter

# Utilizando o Counter

lista = [1, 2, 5, 13, 25, 98, 4, 9, 3, 23, 24, 75, 69, 88, 1, 98, 25, 13, 9]

res = Counter(lista)

print(type(res))

print(res)

print(Counter('Robert Moraes'))

texto = """O método é sempre um aspecto fundamental para o sucesso do produto final, e com o desenvolvimento de software isso não é diferente. Descubra quais são as principais metodologias de desenvolvimento, suas histórias de origem, principais características, curiosidades e muito mais!
No geral, todo software de sucesso costuma ter um processo de desenvolvimento muito bem trabalhado. Mas para gerir um projeto com eficiência, é preciso escolher uma metodologia de software que seja adequada para você e sua empresa."""

palavras = texto.split()

res = Counter(palavras)

print(res.most_common(10))

# Obs: Counter cria para cada elemento da lista foi usando pelo Counter como chave e atribuido a quantidade de ocorrencias de cada elemento.
