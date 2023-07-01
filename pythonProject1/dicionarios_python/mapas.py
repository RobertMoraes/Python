"""
Mapas -> Conhecidos em Python como Dicionarios

Dicionarios em Python são representados por chaves {}

"""
receita = {'jan': 100, 'fev': 250, 'mar': 400}

# Iterar sobre dicionarios
for chave in receita:
    print('Imprimindo chave: ', chave)

for chave in receita:
    print('Imprimindo receita: ', receita[chave])

for chave in receita:
    print(f'Mês: {chave} recebi R$ {receita[chave]}')

print(receita.keys())

for chave in receita.keys():
    print(chave)

print(receita.values())

for valor in receita.values():
    print(valor)

print(receita.items())

for chave, valor in receita.items():
    print(f'Chave ::{chave} e Valor ::{valor}')

print(sum(receita.values()))
print(max(receita.values()))
print(min(receita.values()))
print(len(receita))

