def fun(u_input):
    return (sum([number for number in range(1, u_input) if u_input % number == 0]) == u_input and "YES") or "NO"
print(fun(int(input())))
