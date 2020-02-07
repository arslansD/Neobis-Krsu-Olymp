import math

user_input=int(input(""))
time_seconds=math.floor((user_input%60))
time_hours=((math.floor(user_input/3600)))
time_minutes=math.floor(((user_input-time_seconds)%3600)/60)
print(time_hours, time_minutes, time_seconds)
