lista2 = [12, 19, 28, 14, 31]

print(lista2)
lista2.pop()
lista2.pop()
print(lista2)
#método pop() -> sem valor no parametro, remove o ultimo elemento da lista
#pop(indice): remove por um indice especifico.
lista2.pop(2)
print(lista2)

#remove(remove o elemento): Remove por um elemento especifico
lista2.extend([75, 20, 39])
print(lista2)
lista2.remove(75)
print(lista2)

lista3 = [8, 4, 9, 2, 0, 1]
lista4 = lista3 #as duas se tornam uma variavel
print('Lista 3 -> ', lista3)
print('Lista 4 -> ', lista4)
print('-'*30)
lista4[2] = 6
print('Lista 3 -> ', lista3)
print('Lista 4 -> ', lista4)
lista3 = [8, 4, 9, 2, 0, 1] 
lista4 = lista3.copy() #cria uma copia, uma dependencia inves de atribuir as duas a mesma variavel
lista4[2] = 6
print('Lista 3 -> ', lista3)
print('Lista 4 -> ', lista4)

#exemplo 
varA = 10
varB = varA
print(id(varA), id(varB))
#as duas recebem o mesmo id

#agora se trocarmos o valor da variavel B
varB = 19
print(id(varA), id(varB))
#agora recebem ids diferentesz