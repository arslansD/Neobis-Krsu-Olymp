user_input=input("")
for element in user_input:
  count_letter=user_input.count(element)
  if count_letter>1:
    print("YES")
    break
if count_letter==1:
  print("NO") 
