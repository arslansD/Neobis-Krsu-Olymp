user_input=int(input(""))
def factor(user_input):
  summary=0
  count=2
  if user_input==1:
    print(1)
  elif user_input%2==0:
    while user_input>count:
      summary=count*(count+2)
      count=count+2
    print(summary)
  else:
    count=1
    while user_input>count:
      summary=count*(count+2)
      count=count+2
    print(summary)
factor(user_input)
