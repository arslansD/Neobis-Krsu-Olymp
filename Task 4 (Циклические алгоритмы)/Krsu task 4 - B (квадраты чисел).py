user_input=input("").split()
user_input=list(map(int, user_input))
for element in range (user_input[0], user_input[1]+1):
  print("{}*{}={}".format(element,element, element**2))
