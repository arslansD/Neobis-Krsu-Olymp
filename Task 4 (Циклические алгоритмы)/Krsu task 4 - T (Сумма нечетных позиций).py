user_input=input("")
count=0
summary=0
while count<len(user_input):
  summary=summary+int(user_input[count])
  count=count+2
print(summary)
