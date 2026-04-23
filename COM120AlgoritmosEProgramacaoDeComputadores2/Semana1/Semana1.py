# Tipos Mutáveis e Não Mutáveis em Python

# Quando fazemos uma atribuição:
a = 3
# O objeto int com valor 3 e o nome 'a' são criados.
# O Python mantém em uma tabela todos os nomes de variáveis criadas pelo programa, os quais 'apontam' para 
# os tipos e valores dos objetos alocados na memória

# Exemplos de armazenamento na memória feitos pelo Pyhton
b = 4.0 # Tipo float de valor 4
c = 'hello' # Tipo String de valor 'hello'
d = [2, 3, 5, 8, 11] # Tipo lista de valor [2, 3, 5, 8, 11]

# Caso atribuírmos:
a = 6 
# O valor antigo(3) não será excluído, o que acontece é que será criado um novo objeto e agora a variável 'a'
# aponta para o valor 6.
# int, bool, float, str e complex são imutáveis.

# Já no caso de listas o valor pode ser alterado, caso o valor de 'd' seja alterado
d[3] = 7 # Agora a lista fica [2, 3, 5, 7, 11], o espaço de memória é o mesmo, o valor que foi alterado.

# Caso atribuirmos:
e = a # Tanto a variavél 'a' quanto a 'e' irão apontar para o mesmo endereço de memória.
# Caso 'a' for alterado, 'e' ainda apontara para o valor anterior.

# Caso esse mesmo exemplo for feito com listas
x = [3, 4, 5]
y = x
y[1] = 8

# Tanto o valor de 'x' quanto 'y' ficará [3, 8, 5], ambas serão afetadas, já que a memória é a mesma

# Caso seja uma função

def g(f):
    f = 5

r = 3
g(r)

# Inicialmente ambas tem o mesmo valor e apontam para a mesma coisa, após o valor ser trocado para 'r' elas apontarão para valores
# diferentes