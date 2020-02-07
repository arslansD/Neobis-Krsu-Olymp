first, second = map(str, input().split(" "))

first_m = int(first, 8)
second_m = int(second, 8)

print(str(oct(first_m * second_m)))