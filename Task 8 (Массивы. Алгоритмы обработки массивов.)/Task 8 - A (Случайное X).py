import random
user_input=input().split()
user_input=list(map(int, user_input))
my_list=[]
for element in range(5):
  num=random.randint(1,user_input[0])
  my_list.append(num)
print(my_list)
for element in my_list:
  if element==user_input[1]:
    print(my_list.index(element))
