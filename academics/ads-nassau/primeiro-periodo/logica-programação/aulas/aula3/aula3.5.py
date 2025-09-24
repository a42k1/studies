lista = [8, 5, 2, 0, 9, 4, 2, 2]
#        0  1  2  3  4  5  6  7
#              1           2  3
#index puxa o indice 4 que é o 9
#count puxa a quantidade de vezes que um numero especifico está na lista no caso do 2 ele esta 3 vezes retorna 3
#index(elemento): retorna o indice do elemento buscado.
print(lista.index(9))

#count(elemento): Retorna a quantida de vezes que um elemento esta na lista
quant = lista.count(2)
print(quant)

#saber qual elemento do indice
print(lista.index(lista[5]))
