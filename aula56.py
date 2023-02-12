"""
split e join com list e str 
split - divide uma string 
join - une uma string 
"""
frase = 'Olha só que, coisa interessante'
lista_frases_crua = frase.split(',') # se não passar nada no parenteses ele vai quebrar nos espaços da frase.


lista_frases = []
for i, frase in enumerate(lista_frases_crua):
    lista_frases.append(lista_frases_crua[i].strip()) # strip corta o espeço de uma string aonde estiver espaço ->(rstrip - direita , lstrip - esquerda).

#print(lista_frases_crua)
#print(lista_frases)

frases_unidas = '-'.join(lista_frases) # apenas intereveis 9 string , lista ou tupla
print(frases_unidas)




