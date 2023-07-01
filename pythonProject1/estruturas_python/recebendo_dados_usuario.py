"""
Recebendo dados do usuário

"""
# Entrada de dados
# print("Qual seu nome?")
# nome = input()
nome = input('Qual seu nome?')

# Exemplo de print 'antigo'
# print('Seja bem-vindo(a) %s' % nome)

# Exemplo de print atualizado
# print('Seja bem-vindo(a) {0}'.format(nome))

# Exemplo de print mais atual
print(f'Seja bem-vindo(a) {nome}')

# print("Qual sua idade?")
# idade = input()
idade = int(input('Qual sua idade?'))

# Processamento

# Saída de dados
# Exemplo de print 'antigo'
# print('A %s tem %s anos' % (nome, idade))

# Exemplo de print atualizado
# print('A {0} tem {1} anos'.format(nome, idade))

# Exemplo de print atualizado
print(f'A {nome} tem {idade} anos')

"""
int(idade) => cast

Essa conversão deve ser realizada, pois tudo que é enviado no input é uma String

"""
print(f'A {nome} nasceu em {2023 - idade.__add__(1)}')
