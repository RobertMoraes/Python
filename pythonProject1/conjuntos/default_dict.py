"""
Modulo Collections - Default Dict

Default Dict -> Ao criar um dicionario utilizando-o, informamos um valor default, podendo utilizar um lambda para isso. Este valor sera utilizado sempre que nao houver um valor definido. Caso tentemos acessar uma chave que nao existe, essa chave sera criada e o valor default sera atribuido.

Lambda -> sao funcoes sem nome que podem ou nao receber parametros de entrada e retornar valores.
"""
from collections import defaultdict

dicionario = defaultdict(lambda: 0)

dicionario['curso'] = 'Python'

print(dicionario['curso'])
print(dicionario['outro'])
print(dicionario)
