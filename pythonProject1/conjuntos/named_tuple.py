"""
Modulo Colllections - Named Tuple
tupla = (1, 2, 3)

print(tupla[1])

Named Tuple -> Sao tuplas, diferenciadas, onde, especificamos um nome para a mesma e tambem parametros.
"""
from collections import namedtuple

# Forma 1 - Declaracao Named Tuple

cachorro = namedtuple('cachorro', 'idade raca nome')

# Forma 2 - Declaracao Named Tuple

cachorro = namedtuple('cachorro', 'idade, raca, nome')

# Forma 3 - Declaracao Named Tuple

cachorro = namedtuple('cachorro', ['idade', 'raca', 'nome'])


ray = cachorro(idade=2, raca='Chow-Chow', nome='Zeus')

print(ray.nome)
print(ray.idade)
print(ray.raca)
