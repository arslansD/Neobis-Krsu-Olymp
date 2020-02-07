user_input=input("")
if len(user_input)<=2:
  print()
elif len(user_input)>2:
  count=1
  output=""
  while count<len(user_input)-1:
    output=output+ user_input[count]
    count=count+1

  found=False
  while not found:
    if output[0]!="0":
      print(output)
      found=True
    else:
      output=output.replace("0", "", 1)
      if output=="":
        print()
        break
