user_input=input("").split()
user_input= list(map(int, user_input))
if user_input[0] + user_input[1] + user_input[2] == 180:
  if user_input[0]!=0 and user_input[1]!=0 and user_input[2]!=0:
    print("YES")
  else:
    print("NO")
else:
  print("NO")
