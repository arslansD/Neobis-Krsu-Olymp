user_input=input("").split()
user_input=list(map(int, user_input))
maximum=0
for element in user_input:
  if element > maximum:
    maximum=element
print(maximum)
