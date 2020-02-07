user_input=input("").split()
count=0
space=""
for element in user_input:
  print(count*space, element)
  space="  "
  count=count+1
