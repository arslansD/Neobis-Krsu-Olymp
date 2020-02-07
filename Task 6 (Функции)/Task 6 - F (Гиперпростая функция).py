user_input=input()
def isPrime(user_input):
  score=0
  for element in user_input:
    for elem in range (2,8):
      if int(element)!=elem and int(element)%elem==0:
        score=score+1
  if score>0:
    return ("NO")
  return ("YES")
print(isPrime(user_input))
