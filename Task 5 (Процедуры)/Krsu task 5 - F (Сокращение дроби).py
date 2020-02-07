user_input=input("").split()
user_input=list(map(int, user_input))
found=False
while not found:
  while user_input[0]%2==0 and user_input[1]%2==0:
    user_input[0]=int(user_input[0])//2
    user_input[1]=int(user_input[1])//2
  while user_input[0]%3==0 and user_input[1]%3==0:
    user_input[0]=int(user_input[0])//3
    user_input[1]=int(user_input[1])//3
  while user_input[0]%5==0 and user_input[1]%5==0:
    user_input[0]=int(user_input[0])//5
    user_input[1]=int(user_input[1])//5
  found=True    
print("{}/{}".format(user_input[0], user_input[1]))
