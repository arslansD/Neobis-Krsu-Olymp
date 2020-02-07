user_input=int(input(""))
count=1

while count<user_input:
  number=[]
  test=[]
  for element in str(count):
    number.append(element)
  for elem in str(count**2):
    test.append(elem)

  check=0
  while len(number)!=0:
    if number.pop() == test.pop():
      check=check+1
  if check == len(str(count)):
    print("{}*{}={}".format(count,count,count**2))
  count=count+1
