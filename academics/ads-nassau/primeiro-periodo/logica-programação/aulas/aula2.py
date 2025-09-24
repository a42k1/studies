
# variaveis de entrada

produtos = int(input('Informe a quantidade de produtos maior que zero: '))
if produtos <= 0:
  produtos =  int(input('Por favor, ' 'Insira uma quantidade válida: '))

# variaveis de processamento
extra     = 0
grande    = 0 
media     = 0
pequena   = 0 

while produtos != 0: # repetir enquanto tiver produto (diferente de zero)
  if produtos >= 50:
    extra += 1
    produtos -= 50
  elif produtos >= 20:
    grande += 1
    produtos -=20
  elif produtos >=5:
    media += 1
    produtos -= 5
  elif produtos >= 1:
    pequena += 1
    produtos -= 1
total = extra + grande + media + pequena
print('-' * 20) # multiplica o caractere dentro das aspas por 20
print('Logística de entrega')
print('-' * 20)
print(f'quantidade de caixas extras   {extra}')
print(f'quantidade de caixas grandes  {grande}')
print(f'quantidade de caixas medias   {media}')
print(f'quantidade de caixas pequenas {pequena}')
print('-' * 20)
print(f'Quantidade de caixas usadas {total} ')  
print('-' * 20)