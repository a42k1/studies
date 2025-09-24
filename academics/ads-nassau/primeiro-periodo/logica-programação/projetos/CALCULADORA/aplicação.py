import calculadora
#se eu quiser uma função calculadora especifica utilizar 'from calculadora import somar...'
print('---- Math calculator ----')
print('-'*25)

num1 = int(input('Inform a number: '))
num2 = int(input('Inform another number: '))

opt = input('Inform the desired option (+, -, * ou /))')
if opt ==  '+':
 result = calculadora.summ(num1, num2)
 print('The summ was: ', result)
elif opt == '-':
  result = calculadora.subtract(num1, num2)
  print('The subtraction was: ', result)
elif opt == '/':
  result = calculadora.div(num1, num2)
  print('The division was: ', result)
elif opt == '*':
  result = calculadora.mult(num1, num2)
  print('The multiplication was: ', result)
