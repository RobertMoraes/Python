"""
Modulo Collections: Ordered Dict

dicionario = {'a': 1, 'b': 2, 'c': 3, 'd': 4, 'e': 5}

print(dicionario)

dicionario['f'] = 6
dicionario['g'] = 7

print(dicionario)

for chave, valor in dicionario.items():
    print(f'chave={chave}>>>>valor={valor}')

OrderedDict -> Dicionario que grante a inserção dos elementos.

dicionario = OrderedDict({'a': 1, 'b': 2, 'c': 3, 'd': 4, 'e': 5})

for chave, valor in dicionario.items():
    print(f'chave={chave}>>>>valor={valor}')

"""
from collections import OrderedDict

dict1 = {'a': 1, 'b': 2}
dict2 = {'b': 2, 'a': 1}

print(dict1 == dict2)  # True -> Pois não há validação da ordem somente valores continos no dicionario.

odict1 = OrderedDict({'a': 1, 'b': 2})
odict2 = OrderedDict({'b': 2, 'a': 1})

print(odict1 == odict2)  # False -> Pois alem de ser validado os valores é realizado a validação das ordem do dicionario.
