user_input=input("").split()
user_input=list(map(int,user_input))
Sequence=(user_input[1]-user_input[0])*(user_input[2]-1)+user_input[0]
print(Sequence)
