import random
my_list=[random.randint(-100,100) for element in range(int(input()))]

maximum=max(my_list)
minimum=min(my_list)
max_index = None
min_index = None
print(' '.join(list(map(str, my_list))))
for counter, elem in enumerate(my_list):
  if elem == maximum and max_index == None:
    max_index = counter
  elif elem == minimum and min_index == None:
    min_index = counter
  else:
    pass
print(minimum, min_index)
print(maximum, max_index)
