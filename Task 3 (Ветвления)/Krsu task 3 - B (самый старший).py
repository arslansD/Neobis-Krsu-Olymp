user_input=input("").split()
user_input=list(map(int, user_input))
names=["Anton", "Boris", "Victor"]
if user_input[0]==user_input[1] and user_input[1]==user_input[2]:
  print("Same age")
elif user_input[0]==user_input[1] and user_input[0]>user_input[2]:
  print("Victor")
elif user_input[1]==user_input[2] and user_input[2]>user_input[0]:
  print("Anton")
elif user_input[0]==user_input[2] and user_input[0]>user_input[1]:
  print("Boris")
else:
  maximum=max(user_input)
  if user_input[0]==maximum:
    print("Anton")
  elif user_input[1]==maximum:
    print("Boris")
  elif user_input[2]==maximum:
    print("Victor")
