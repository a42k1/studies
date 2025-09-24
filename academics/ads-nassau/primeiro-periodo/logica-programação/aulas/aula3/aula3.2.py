lista3 = [8, 4, 9, 2, 0, 1] 
lista4 = lista3.copy() #cria uma copia, uma dependencia inves de atribuir as duas a mesma variavel

lista3.sort()
print(lista3) #Ordena definitivamente de forma crescente isso nao tem volta

lista3.sort(reverse = True) #Ordena de forma decrescente >DEFINITIVAMENTE<
print(lista3) 
print(lista4)
lista3.reverse()
print(lista3)