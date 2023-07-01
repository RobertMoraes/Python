"""
Estruturas condicionais
if, else, elif

"""

idade = 14

if idade < 13:
    print('Entrada proibida')
elif idade < 18:
    print('Entrada somente com responsável')
else:
    print('Maior de idade, entrada liberada')

mes = 'junho'
meses = mes.upper()
print(meses)
numMes = 0

if meses == 'ABRIL':
    numMes = 4
    print(f'{numMes} {meses}')
elif meses == 'MAIO':
    numMes = 5
    print(f'{numMes} {meses}')
elif meses == 'JUNHO':
    numMes = 6
    print(f'{numMes} {meses}')
else:
    print('aleatorio')

