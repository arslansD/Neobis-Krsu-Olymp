user_input=input("").split()
user_input=list(map(int, user_input))
if user_input[0]==user_input[1] and user_input[1]==user_input[2]:
  print(3)
elif (user_input[0]==user_input[1] and user_input[0]!=user_input[2]) or (user_input[1]==user_input[2] and user_input[1]!=user_input[0]):
  print(2)
else:
  print(1)
