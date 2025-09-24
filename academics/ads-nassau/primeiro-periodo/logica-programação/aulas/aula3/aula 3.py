# Criando uma lista vazia
lista1 = []

# append(elemento): inserir um elemento ao final da lista.
lista1.append(12)
lista1.append(20)
lista1.append(32)
print(lista1)

# insert (indice, elemento): inserir um elemento em um indice especifico.
lista1.insert(1, 17)
print(lista1)
lista1.insert(0, 28)
print(lista1)
lista1.insert(3, 10)
print(lista1)

lista1.append([5, 10, 20])
print(lista1)
print(lista1[6])

# extend(coleção): inserir uma coleção de dados de forma individual
lista1.extend([23, 18, 29])
print(lista1) #alternativa ao append quando quiser inserir varios items à lista de maneira individual.
lista2 = 10, 8, 12
lista1.insert(2, lista2)
print(lista1)
