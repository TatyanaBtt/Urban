# 1.Функция с параметрами по умолчанию:
def print_params(a = 1, b = 'строка', c = True):
    print(a, b, c)

print_params(b = 25)
print_params(c = [1, 2, 3])

# 2.Распаковка параметров:
value_list = [18, False, 'Осень']
value_dict = {'a' : 'Params', 'b' : 45, 'c' : True}

print_params(*value_list)
print_params(**value_dict)

# 3.Распаковка + отдельные параметры:
values_list_2 = [25, 'Сентябрь']
print_params(*values_list_2, 42)

