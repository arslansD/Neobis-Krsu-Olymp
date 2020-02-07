user_input=input("")
found=False
count=1
while count<len(user_input) and not found:
  if user_input[count-1]==user_input[count]:
    print("YES")
    found=True
  count=count+1
if found==False:
  print("NO")
