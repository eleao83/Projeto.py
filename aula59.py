# Desempacotamento em chamadas 
# de métados e funções
string = 'ABCD'
lista = ['Maria', 'Helena',1, 2, 3, 'Eduarda']
tupla = 'Python', 'é', 'legal'
""" 
p, b, *_, ap, u = lista
print(a, u, ap) """

""" for nome in lista:
    print(nome, end=' ') """


""" print('Maria', 'Helena',1, 2, 3, 'Eduarda')
print(*lista)   # desempacotamento de iteravel  
print(*string)
print(*tupla) """

salas = [
    # 0         1
    ['Maria', 'Helena', ], # 0
    # 0
    ['Eliane', ], # 1
    # 0       1       2   
    ['Luiz', 'João', 'Eduarda', ], # 2
]

print(*salas, sep='\n')

