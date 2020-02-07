user_input=input("").split()
user_input=list(map(int, user_input))
time_seconds=user_input[2]+(user_input[1]*60)+(user_input[0]*60*60)
print(time_seconds)
