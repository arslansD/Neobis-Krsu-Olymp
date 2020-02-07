import random
my_list=[random.randint(1,5) for element in range (6)]
for element in my_list:
  print(element, end=" ")

count=0
Check=False
while count+1<len(my_list):
  if my_list[count]==my_list[count+1]:
    print("\nYES", end=" ")
    print(count, end=" ")
    print(count+1, end = " ")
    Check=True
  count=count+1
if count+1==len(my_list) and not Check:
  print("\nNO")