user_input=list(map(int, input().split()))
first, second = user_input[0], user_input[1]
def check (first, second):
  result="YES"
  for element in range (2,10):
    if first%element==0 and second%element==0:
      result="NO"
  return result
print(check(first, second))
