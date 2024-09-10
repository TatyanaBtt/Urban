immutable_var = 1,21,'var',True
print(immutable_var)
#immutable_var[1] = 121   - данная операция выдаст ошибку, так как кортеж является неизменяемым объектом.
# текст ошибки подскажет, что объект кортежа не поддерживает назначения элементов.
mutable_list = [23,17,'work',False]
print(mutable_list)
mutable_list.remove(False)
print(mutable_list)
mutable_list[2] = True
print(mutable_list)
