user_input=int(input(""))
def check(user_input):
  if user_input%4==0 and user_input%400==0 and user_input%100!=0:
    print("YES")
  else:
    print("NO")
check(user_input)
