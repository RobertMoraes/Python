"""
Modulo Colllections - Named Tuple
tupla = (1, 2, 3)

print(tupla[1])

Named Tuple -> Sao tuplas, diferenciadas, onde, especificamos um nome para a mesma e tambem parametros.
Documentation: https://docs.python.org/3/library/collections.html#collections.namedtuple
"""
from collections import namedtuple

# Forma 1 - Declaracao Named Tuple

cachorro = namedtuple('cachorro', 'idade raca nome')

# Forma 2 - Declaracao Named Tuple

cachorro = namedtuple('cachorro', 'idade, raca, nome')

# Forma 3 - Declaracao Named Tuple

cachorro = namedtuple('cachorro', ['idade', 'raca', 'nome'])


ray = cachorro(idade=2, raca='Chow-Chow', nome='Zeus')

# Acessando os dados

# Forma 1
print(ray[0])
print(ray[1])
print(ray[2])

# Forma 2 - Melhor forma
print(ray.nome)
print(ray.idade)
print(ray.raca)
