user_input=input("")
summary=0
if len(user_input)%2!=0:
  for element in user_input:
    summary=summary+int(element)
else:
  count=0
  while count<len(user_input)/2:
    summary=summary+int(user_input[count])
    count=count+1
print(summary)
