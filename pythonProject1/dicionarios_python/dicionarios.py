"""
Dicionarios

OBS: Em algumas linguagens de programação, os dicionários Python são conhecidos por mapas.

Dicionários são coleções do tipo chave/valor

Dicionários são representados por chaves{}
"""
print(type({}))

print(':::::::::: Criacao de dicionários ::::::::::')

# Forma 1 - Mais comum
paises = {'br': 'Brasil', 'eua': 'Estados Unidos', 'py': 'Paraguai'}

print(paises)
print(type(paises))

# Forma 2 - Menos comum
paises = dict(br='Brasil', eua='Estados Unidos', py='Paraguai')

print(paises)
print(type(paises))

print(':::::::::: Acessando elementos ::::::::::')

# Forma 1 - Acessando via chave, da mesma forma que lista/tupla
print(paises['br'])
print(paises['py'])

# Forma 2 - Acessando via get - Recomendado
print(paises.get('py'))
print(paises.get('ru'))
print(paises.get('br'))

pais = paises.get('ru', 'Não encontrado!')

print(f'Pais: {pais}')

print('Brasil' in paises)
print('ru' in paises)
print('br' in paises)

# Dicionario pode receber qualquer tipo de variavel

localidades = {
    (12.5686, 16.1586): 'São Mateus',
    (15.5686, 18.1586): 'Mooca',
    (13.5686, 17.1586): 'Belenzinho',
}

print(localidades)
print(type(localidades))

# Adicionar elementos no dicionario

receita = {'jan': 100, 'fev': 300, 'mar': 450}

print(receita)

# Forma 1 - Mais comum

receita['abr'] = 250

print(receita)

# Forma 2

nova_receita = {'mai': 600}
receita.update(nova_receita)

print(receita)

# Atualizando dados em um dicionario

# Forma 1

receita['mai'] = 550

print(receita)

# Forma 2

receita.update({'mai': 570})

print(receita)

# CONCLUSAO 1: A forma de adicionar novos elementos ou atualizar dados em um dicionario é a mesma
# CONCLUSAO 2: Em dicionarios, NAO podemos ter chaves repetidas

# Remover dados de um dicionario

# Forma 1 - Mais comum
ret = receita.pop('mar')
print(ret)
print(receita)

# Obs: para remover um dado de um dicionario é necessario passar a chave, caso contrario retornará um KeyError
# Obs2: ao remover um objeto com pop, o valor do objeto sempre será retornado

# Forma 2
del receita['fev']

print(receita)

# Obs: caso a chave não exista retorna um KeyError e nao retorna valor igual o pop
"""
Carrinho de compras:
    Produto 1:
        - nome;
        - qtde;
        - preco;
    Produto 2:
        - nome;
        - qtde;
        - preco;
        
Poderiamos utilizar uma lista para isso? Sim 
"""
print('::::: Carrinho de compra - Lista :::::')

carrinho = []
produto1 = ['PlayStation 5', 1, 3999.00]
produto2 = ['Monitor LG 34"', 2, 3599.00]

carrinho.append(produto1)
carrinho.append(produto2)

print(carrinho)

print('::::: Carrinho de compra - Tupla :::::')

produto1 = ('PlayStation 5', 1, 3999.00)
produto2 = ('Monitor LG 34"', 2, 3599.00)

carrinho = (produto1, produto2)

print(carrinho)

print('::::: Carrinho de compra - Dicionario :::::')

carrinho = []

produto1 = {'nome': 'PlayStation 5', 'qtde': 1, 'preco': 3999.00}
produto2 = {'nome': 'Monitor LG 34"', 'qtde': 2, 'preco': 3599.00}

carrinho.append(produto1)
carrinho.append(produto2)

print(carrinho)

print(carrinho[0])
print(carrinho[0].get('preco') + carrinho[1].get('preco'))
print(produto1.get('preco')+produto2.get('preco'))

print('::::: Metodos de Dicionarios :::::')
# Metodos de dicionarios
d = dict(a=1, b=2, c=3)
print(d)
print(type(d))

# Limpar dicionario
e = d.copy()
print(e)
e.clear()
print(e)
print(d)

# Copiando um dicionario para outro
novo = d.copy()  # Deep copy
print(novo)
novo['d'] = 4
print(d)
print(novo)

novo2 = d  # Shallow copy
print(novo2)
novo2['d'] = 4
print(d)
print(novo2)

# Forma nao usual de criacao de dicionarios
# Obs: metodo fromkeys recebe dois parametros: um iteravel e um valor.
# Ele vai gerar para cada valor do iteravel uma chave e ira atribuir a esta chave o valor informado.

outro = {}.fromkeys('a', 'b')
print(outro)
print(type(outro))

usuario = {}.fromkeys(['nome', 'pontos', 'email', 'profile'], 'desconhecido')
print(usuario)
print(type(usuario))

veja = {}.fromkeys('teste', 'valor')
print(veja)

veja = {}.fromkeys(range(1, 11), 'novo')
print(veja)
