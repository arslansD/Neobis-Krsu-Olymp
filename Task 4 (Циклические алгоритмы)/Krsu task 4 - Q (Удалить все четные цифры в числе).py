user_input=input("")
for element in user_input:
  if int(element)%2 ==0:
    user_input=user_input.replace(element, "")
print(user_input)
