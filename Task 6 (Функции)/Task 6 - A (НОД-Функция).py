def my_freaking_GCD(a, b): 
  
  while(b): 
    a, b = b, a % b        
  print("GCD({},{})={}".format(user_input[0], user_input[1], a))
  
user_input=input().split()
user_input=list(map(int, user_input))  
a = user_input[0]
b= user_input[1]
my_freaking_GCD(a,b)