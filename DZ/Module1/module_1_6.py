my_dict = {'Anna':1999,'Sergey':2001,'Tatyana':1990,'Nastya':2006}
print(my_dict)
print(my_dict['Anna'])
print(my_dict.get('Fedor', 'Такого ключа нет.'))
my_dict.update({'Fedor':1980,
                'Alex':1985})
print(my_dict.pop('Anna'))
print(my_dict)

my_set = {22,33,1,2,3,2,1,'string','key',22,2,3,'key'}
print(my_set)
my_set.update([12,'Hello!'])
my_set.remove(22)
my_set.discard(44)
print(my_set.pop())
print(my_set)
