"""
Estruturas Lógicas: and, or, not, is

Operadores unários:
    - not;
Operadores binários:
    - and, or, is
"""
ativo = False
logado = False

print('CASE 1 - AND')
if ativo and logado:
    print('Bem-vindo(a) usuário(a)!')
else:
    print('Você precisa ativar sua conta. Por favor, verifique seu e-mail.')

print('CASE 2 - OR')
if ativo or logado:
    print('Bem-vindo(a) usuário(a)!')
else:
    print('Você precisa ativar sua conta. Por favor, verifique seu e-mail.')

print('CASE 3 - NOT')
if not ativo:
    print('Você precisa ativar sua conta. Por favor, verifique seu e-mail.')
else:
    print('Bem-vindo(a) usuário(a)!')

print('CASE 4 - IS')
if ativo is False:
    print('Você precisa ativar sua conta. Por favor, verifique seu e-mail.')
else:
    print('Bem-vindo(a) usuário(a)!')
