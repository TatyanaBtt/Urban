calls = 0
def count_calls():
    global calls
    calls += 1

def string_info(string):
    count_calls()
    len_str = len(string)
    apper_str = string.upper()
    lower_str = string.lower()
    return  (len_str, apper_str, lower_str)

def is_contains(string, list_to_search):
    count_calls()
    return string.lower() in (s.lower() for s in list_to_search)

print(string_info('Лукоморье'))
print(string_info('Регистрация'))
print(string_info('Аванс'))
print(is_contains('Лукоморье',['Море','Лук','луКОШко']))
print(is_contains('Аванс',['снава','аВаНс','регистрация']))

print(calls)

