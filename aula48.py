"""
Listas em Python
Tipo list - Mutável
Suporta vários valores de qualquer tipo
Conhecimentos reutilizáveis - índices e fatiamento
Métodos úteis: append, insert, pop, del, clear, extend, +
"""
#        +01234
#        -54321
""" Parte 1
string = 'ABCDE'  # 5 caracteres (len)
# print(bool([]))  # falsy
# print(lista, type(lista))

#        0    1      2              3    4
#       -5   -4     -3             -2   -1
lista = [123, True, 'Luiz Otávio',  1.2, []]
lista[-3] = 'Maria'
print(lista)
print(lista[2], type(lista[2]))
"""
""" Parte 2
Listas em Python
Tipo list - Mutável
Suporta vários valores de qualquer tipo
Conhecimentos reutilizáveis - índices e fatiamento
Métodos úteis:
    append, insert, pop, del, clear, extend, +
Create Read Update   Delete
Criar, ler, alterar, apagar = lista[i] (CRUD)

#        0   1   2   3   4   5
lista = [10, 20, 30, 40]
# lista[2] = 300
# del lista[2]
# print(lista)
# print(lista[2])
lista.append(50)
lista.pop() # remove o último elemento da lista
lista.append(60)
lista.append(70)
ultimo_valor = lista.pop(3)
print(lista, 'Removido,', ultimo_valor)

# Parte 3
#        0    1   2   3 indice 
lista = [10, 20, 30, 40]
lista.append('Luiz') # foi add no final da lista
nome = lista.pop() # pop remove o último item da lista, caso não passse o indice ele reordena o indice.
print(lista)
del lista[-1] # -1 deleta o último número da lista
#lista.clear() limpa a lista
lista.insert(0, 5) # é um metado que recebe dois argumento 1º indice 2º o valor para add.
print(lista) 
"""
""" Parte 4
Listas em Python
Tipo list - Mutável
Suporta vários valores de qualquer tipo
Conhecimentos reutilizáveis - índices e fatiamento
Métodos úteis:
    append - Adiciona um item ao final
    insert - Adiciona um item no índice escolhido
    pop - Remove do final ou do índice escolhido
    del - apaga um índice
    clear - limpa a lista
    extend - estende a lista
    + - concatena listas
Create Read Update   Delete
Criar, ler, alterar, apagar = lista[i] (CRUD)

lista_a = [1, 2, 3]
lista_b = [4, 5, 6]
lista_c = lista_a + lista_b
lista_a.extend(lista_b)
print(lista_a)
"""

""" Parte 5
Cuidados com dados mutáveis
= - copiado o valor (imutáveis)
= - aponta para o mesmo valor na memória (mutável)
"""
"""
lista_a = ['Luiz', 'Maria', 1, True, 1.2]
lista_b = lista_a.copy() # aponta para o mesmo valor da memoria da variavel, quando alterar a variavel que foi copiada abaixo no altera.

lista_a[0] = 'Qualquer coisa'
print(lista_a)
print(lista_b)
"""

lista_a = ['Luiz', 'Maria']
lista_b = lista_a # deseja forma ele copia o valor da variavel "A". Ao modificar ele tbm alterar o valor. 
print(lista_a)
print(lista_b)