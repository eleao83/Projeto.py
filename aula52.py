"""
Tipo tupla - Uma lista imutavél. é utilizda quando tem uma lista que não precisa ser alterada.
Como criar uma tupla? Ex: 'Maria', 'Helena', 'Luiz' : só não utilizar os conchetes ou colocar em '()'.
"""
# nomes = ('Maria', 'Helena', 'Luiz')
nomes = ['Maria', 'Helena', 'Luiz'] # criei uma lista
nomes = tuple(nomes) # Alterando lista para tupla
nomes = list(nomes) # Alterando tupla para lista
print(nomes[-1])
print(nomes)
