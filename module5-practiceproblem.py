def unique(input_list=[]):
  to_return = []
  for el in input_list:
    if el not in to_return:
      to_return.append(el)
  return to_return
  
print(unique([1, 1, 4, 5, 1]))  


def unique(input_list=[]):
  to_return = []
  for el in input_list:
    if el not in to_return:
      to_return.append(el)
  return to_return
  
print(unique(['Mark', 'Mark', 'John', 'Anne'])) 