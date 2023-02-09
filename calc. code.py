while True:
#take inputs of operators and operand
  number1 = int(input('enter first number: '))
  number2 = int(input('enter second number: '))
  #lets take operator
  operator = input('enter the operator: ')
  #lets print the type of the variables
  #print(type(number1), type(number2), type(operator))
  result = ' ' 
  if operator == '+':
   result = number1+number2
  elif operator == '-':
    result = number1-number2
  elif operator == '*':
   result = number1*number2
  elif operator == '/':
    result = number1/number2 
  else:
   print('not identified')
    #lets print the results 
  print('the result is : ',result) 