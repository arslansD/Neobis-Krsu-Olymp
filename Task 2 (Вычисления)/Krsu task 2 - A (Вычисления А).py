user_input=input().split()
user_input=list(map(int, user_input))
addition=user_input[0]+user_input[1]+user_input[2]
multicast=user_input[0]*user_input[1]*user_input[2]
division=((user_input[0]+user_input[1]+user_input[2])/3)
print("{}+{}+{}={}".format(user_input[0], user_input[1], user_input[2], addition ))
print("{}*{}*{}={}".format(user_input[0], user_input[1], user_input[2], multicast))
print("({}+{}+{})/3={}".format(user_input[0], user_input[1], user_input[2], round(division, 3)))
