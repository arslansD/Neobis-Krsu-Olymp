user_input=input("").split()
user_input=list(map(int, user_input))

for element in range (user_input[0], user_input[1]+1):
  if element == 2 or element==3 or element==5:
    print(element, end=" ")
  elif element == 1:
    continue
  check=0
  if element%2!=0:
    check=check+1
  if element%3!=0:
    check=check+1
  if element%5!=0:
    check=check+1
  if check>2:
    print(element, end=" ")
