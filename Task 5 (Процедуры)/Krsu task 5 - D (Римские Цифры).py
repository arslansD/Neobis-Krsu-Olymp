from collections import OrderedDict

def write_roman(user_input):
    number = OrderedDict()
    number[1000] = "M"
    number[900] = "CM"
    number[500] = "D"
    number[400] = "CD"
    number[100] = "C"
    number[90] = "XC"
    number[50] = "L"
    number[40] = "XL"
    number[10] = "X"
    number[9] = "IX"
    number[5] = "V"
    number[4] = "IV"
    number[1] = "I"

    def roman_num(user_input):
        for element in number.keys():
            x, y = divmod(user_input, element)
            yield number[element] * x
            user_input = user_input - (element * x)
            if user_input <= 0:
                break

    return "".join([elem for elem in roman_num(user_input)])

user_input=int(input(""))
write_roman(user_input)
