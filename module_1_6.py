my_dict = {'Oleg': 2005, 'Denis': 2004, 'Danil': 2001}
print(my_dict)
print(my_dict['Oleg'])
my_dict.update({'Vadim': 2003,
                'Max': 20006})
del my_dict['Oleg']
print(my_dict)
print(end='\n')
my_set = {1, 1, 1, 2, 3, 3, 'Red', 'Red', (2, 3), (2, 3)}
print(my_set)
my_set.update({65, 378})
my_set.discard('Red')
print(my_set)