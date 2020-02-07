user_input=int(input(""))
if user_input<1 or user_input>12:
  print("Wrong number")
elif user_input>=3 and user_input<=5:
  print("Spring")
elif user_input>=6 and user_input<=8:
  print("Summer")
elif user_input>=9 and user_input<=11:
  print("Autumn")
else:
  print("Winter")
