user_input=input("").split()
user_input=list(map(int, user_input))
if (user_input[0]+user_input[1])>=user_input[2] and (user_input[1]+user_input[2])>=user_input[0] and (user_input[0]+user_input[2])>=user_input[1]:
  print("YES")
else:
  print("NO")
