"""
Definindo funções

- Funções são pequenos partes de código que realizam tarefas específicas;
- Pode ou não receber entrada de dados e retornar uma saída de dados;
- Muito uteis para executar procedimentos similares por repetidas vezes;

OBS: Se houver criado uma função que realize diversas tarefas dentro dela,
    melhor refatorar para que ela fique mais simplificada.

Já utilizamos várias funções desde o inicio do curso:
- print()
- len()
- max()
- min()
- count() entre outras;
"""
# Exemplo de utilização de funções:

cores = ['verde', 'amarelo', 'azul', 'branco']

# Utilizando a função integrada(Built-in) do Python print()

print(cores)

cores.append('roxo')

print(cores)

curso = 'Programação em Python: Essencial'

print(curso)

"""
Em Python, a forma geral de definir uma função é:

def nome_da_funcao(parametros_de_entrada):
    bloco_da_funcao
    
Onde:

nome_da_funcao -> SEMPRE, com letras minusculas, e se for nome composto, separado por underline(Snake Case);
parametros_de_entrada -> Opcionais, onde tendo mais de um, cada um separado por virgula, podendo ser opcionais ou não;
bloco_da_funcao -> Também chamado de corpo da funcao ou implementacao, é onde o processamento da funcao acontece.
Neste bloco, pode ter ou não retorno da funcao.

OBS: Veja que para definir uma funcao, utilizamos a palavra reservada 'def' informando ao Python que estamos definindo
uma funcao. Também abrimos o bloco de codigo com o ja conhecido dois pontos ':' que é utilizado em Python para definição
de blocos.
"""


# Definindo a primeira funcao

def diz_oi():
    print('Olá Mundo!')


"""
OBS:

1 - Veja que dentro das nossas funções podemos utilizar outras funções;
2 - Veja que nossa função só executa 1 tarefa, ou seja, a unica coisa que ela faz é imprimir a mensagem 'Olá Mundo!';
3 - Veja que esta funcao não recebe nenhum parametro de entrada;
4 -  Veja que esta funcao não retorna nada;
"""
# Chamando a funcao criada
diz_oi()

"""
OBS:

Para chamar qualquer funcao sempre colocar o parenteses no final da funcao 'diz_oi()'
"""


def cantar_parabens():
    print('Parabéns para você')
    print('Nesta data querida')
    print('Muitas felicidades')
    print('Muitos anos de vida!')


# for n in range(5):
#     print(n)
#     cantar_parabens()

canta = cantar_parabens

canta()
