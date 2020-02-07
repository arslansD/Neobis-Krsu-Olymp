user_input=input("")
mylist=[]
for element in user_input:
  mylist.append(element)
summary=0
for element in mylist:
  summary=int(element)+summary
print(summary)
