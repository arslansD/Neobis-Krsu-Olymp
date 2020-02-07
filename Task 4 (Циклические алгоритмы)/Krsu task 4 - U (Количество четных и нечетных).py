user_input=input("")
count=0
chet=0
nechet=0
while count<len(user_input):
  if int(user_input[count])%2!=0:
    nechet=nechet+1
  else:
    chet=chet+1
  count=count+1
print(nechet, chet)
