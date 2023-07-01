"""
Tipo string

Em Python, um dado é considerado um tipo string sempre que:

— Estiver entre àspas simples >>> 'uma string', '234', 'a', 'True', '42.3'
— Estiver entre àspas duplas >>> "uma string", "234", "a", "True", "42.3"
— Estiver entre àspas simples triplas >>> '''uma string''', '''234''', '''a''', '''True''', '''42.3'''
"""
# Estiver entre àspas duplas triplas >>> """uma string""", """234""", """a""", """True""", """42.3"""

nome1 = """Robert Moraes"""
nome2 = '''Robert Moraes'''
nome3 = 'Robert Moraes'
nome4 = "Robert Moraes"

print(f'Àspas duplas triplas {nome1}')
print(type(nome1))
print(f'Àspas simples triplas {nome2}')
print(type(nome2))
print(f'Àspas simples {nome3}')
print(type(nome3))
print(f'Àspas duplas {nome4}')
print(type(nome4))

print(nome1.upper())
print(nome1.lower())
print(nome1.split())
print(nome1[0])
print(nome1[0:6])
print(nome1[5::-1])



