user_input=input("").split()
user_input=list(map(int, user_input))
count=0
total=0
if (user_input[0]>0 and user_input[1]>0) or (user_input[0]<0 and user_input[1]<0):
  while count<abs(user_input[0]):
    total=total+user_input[1]
    count=count+1
  print(abs(total))
else:
  while count<max(user_input[0], user_input[1]):
    total=total+(min(user_input[0], user_input[1]))
    count=count+1
  if user_input[0]<0:
    user_input[0]="("+str(user_input[0])+")"
    print("{}*{}={}".format(user_input[0], user_input[1], total))
  else:
    user_input[1]="("+str(user_input[1])+")"
    print("{}*{}={}".format(user_input[0], user_input[1], total))
