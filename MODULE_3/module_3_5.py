def get_multiplied_digits(number):
    str_number = str(abs(number))
    first = int(str_number[0])
    number_1 = str_number.replace('0', '1')
    if len(str_number) <= 1:
        return first
    else:
        return first * get_multiplied_digits(int(number_1[1:]))

rezalt1 = get_multiplied_digits(-60203250)
print(rezalt1)
