"""
enumerate - enumera iteráveis (índices)
enumerate  - o ideal não é jogar dentro de uma variavel e sim joga o valor direto EX: no (for)
\n -> quebra a linha --- \t é um 'tab'
"""
lista = ['Maria', 'Helena', 'Luiz']
lista.append('João')

for indice, nome in enumerate(lista):
    print(indice, nome, lista[indice])

"""
lista_enumerada = enumerate(lista)
lista_enumerada = list(enumerate(lista, start=3)) # com start ele inicia apartir do indice passado.

#print(next(lista_enumerada))

for item in lista_enumerada:
    print(item)
"""
""" Ex 1 
for item in enumerate(lista):
    indice, nome = item # desenpacotando valores.
    print(indice, nome)
"""
"""
# Ex 2 Desepacontamento direto no for 

for indice , nome in enumerate(lista):
    print(indice, nome)

# Ex 3 for dentro do outro.
for tupla_enumerada in enumerate(lista):
    print('For da tupla:')
    for valor in tupla_enumerada:
        print(f'\t{valor}')
"""

