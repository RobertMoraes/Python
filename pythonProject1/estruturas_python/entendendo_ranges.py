"""
Ranges

- Precisamos conhecer o loop for para usar os ranges.
- Precisamos conhecer o range para trabalhar melhor com loop for.

Ranges são utilizados para gerar sequencias numericas, não de forma aleatoria, mas sim de maneira especificada.

Formas gerais:

# Forma 1

range(valor_de_parada)

OBS: valor_de_parada não inclusive (inicio padrao 0, e passo de 1 em 1)

# Exemplo Forma 1
for num in range(11):
    print(num)

# Forma 2

range(valor_de_inicio, valor_de_parada)

OBS: valor_de_parada não inclusive (inicio especificado pelo usuario, e passo 1 em 1)

# Exemplo Forma 2
for num in range(4, 11):
    print(num)

# Forma 3

range(valor_de_inicio, valor_de_parada, passo)

OBS: valor_de_parada não inclusive (inicio especificado pelo usuario, e passo especificado pelo usuario)

# Exemplo Forma 3
for num in range(0, 21, 2):
    print(num)

# Forma 4 (Inversa)

range(valor_de_inicio, valor_de_parada, passo)

OBS: valor_de_parada não inclusive (valor_de_inicio especificado pelo usuario, e passo especificado pelo usuario)

# Exemplo Forma 4
for num in range(50, 0, -5):
    print(num)

"""
# Exemplo 1
# for num in range(11):
#     print(num)

# Exemplo 2
# for num in range(4, 11):
#     print(num)

# Exemplo 3
# for num in range(0, 21, 2):
#     print(num)

# Exemplo 4
# for num in range(50, 0, -5):
#     print(num)
