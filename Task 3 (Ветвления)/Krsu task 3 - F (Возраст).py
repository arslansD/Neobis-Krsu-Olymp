user_input=input("")
answer=""
check=[20,30,40,50,60,70,80,90,100,110,120]
if int(user_input) == 1:
  answer="год."
if int(user_input) in range(5, 13) or int(user_input[1]) in range (5,10):
  answer="лет."

if (int(user_input) in range(2,5)) or (user_input[1] in "234" and (int(user_input) not in check)):
  answer="года."

if user_input[1] in '01' and (user_input[0] in range (2,9) or user_input=='101'):
  answer="год."

if (user_input[1]=='1' and (int(user_input[2]) in range(5,10))) or (int(user_input) in check) or (user_input[2] in "234") or user_input=='111':
  answer="лет."

print("Вам", user_input, answer)

#https://docs.python.org/2/library/locale.html
