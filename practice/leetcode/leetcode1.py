def roman_to_int(input_roman):
    roman_numbers = ['I', 'V', 'X', 'L', 'C', 'D', 'M']
    roman_numbers_value = [1, 5, 10, 50, 100, 500, 1000]

    total = 0
    
    for i in range(len(input_roman)):
        index =
roman_numbers.index(input_roman[i])
        value =
roman_numbers_value[index]

     if i == len(input_roman) - 1:
      total += value
      break

      index_next = roman_numbers.index(input_roman[i + 1])
      value_next = roman_numbers_value[index_next]

      if value < value_next:
        total -= value
      else:
        total += value
    return total