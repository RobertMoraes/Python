print('::::: TABUADA USANDO WHILE :::::')

num = 0
tabuada = int(input('Informe a tabuada: '))
while num <= 10:
    print(f'{num}*{tabuada}={num*tabuada}')
    num += 1

print('::::: TABUADA USANDO FOR :::::')

numero = 0
for numero in range(0, 11):
    print(f'{numero}*{tabuada}={numero*tabuada}')

