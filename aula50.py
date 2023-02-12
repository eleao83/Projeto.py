"""
Exercício
Exiba os índices da lista
"""

lista = ['Maria', 'Helena', 'Luiz']
lista.append('João') # Add na informacão ao final da lista.
indices = range(len(lista)) # variavel para enuremar os indeces.

for indece in indices: 
    print(indece, lista[indece], type(lista[indece]))
    
