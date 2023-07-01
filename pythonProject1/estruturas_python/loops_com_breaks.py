"""
Saindo de loops com break

Funciona da mesma maneira que em Java ou C.

Utilizamos o break para sair de loops de maneira projetada.

"""
# Exemplo 1
for num in range(1, 11):
    if num == 6:
        print(f'Valor {num} foi encontrado!')
        break
    else:
        print(num)

# Exemplo 2
# while True:
#     comando = int(input("Precione '0' para sair: "))
#     if comando == 0:
#         break

while True:
    comando = input("Precione 'sair' para sair: ").lower()
    if comando == 'sair':
        break
