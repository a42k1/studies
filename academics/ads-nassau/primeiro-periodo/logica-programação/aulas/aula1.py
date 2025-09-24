
# Variavel vai guardar a quantidade de notas, começa zerado
contador = 1
menor_nota = None 
maior_nota = None
soma_notas = 0

# Repetição para medir as 6 notas
while contador <=6:
  # Pedir nota
  nota = float(input(f'Informe {contador}ª a nota: '))
  if nota > 10:
    print("Nota inválida. Encerrando o programa.")
    exit ()
     
  soma_notas += nota

  if contador == 1: 
    maior_nota = nota
    menor_nota = nota
  else:
    # Verificar se a nova nota é a menor
    if nota < menor_nota:
      menor_nota = nota
    # Verificar se a nova nota é a maior
    elif nota > maior_nota:
      maior_nota = nota
  # Incrementar ao contador
  contador += 1
# Calcular a média
media = (soma_notas - maior_nota - menor_nota) / 4
#Exibir Resultados
print(f'O resultado é {media:.1f}.')
  






