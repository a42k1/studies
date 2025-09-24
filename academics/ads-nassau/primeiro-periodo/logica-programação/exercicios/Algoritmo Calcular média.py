try:
  nota_1 = float(input('Digite a AV1: '))
  nota_2 = float(input('Digite a AV2: '))
  nota_3 = float(input('Digite a AV3: '))
  nota_4 = float(input('Digite a AV4: '))
  media = (nota_1 + nota_2 + nota_3 + nota_4) / 4
  print(f'A média do aluno é: {media:.2f}')
except ValueError:
  print('Nota máxima é 10')