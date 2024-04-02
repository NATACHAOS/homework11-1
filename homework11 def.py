def print_params(a=1, b="str", c=True):
    print(a, b, c)


print_params(b = 25)  # ok
print_params( 'a',  '',  '')  # теперь работает
print_params('', '', '')
print_params()  # теперь работает
print_params(c = [1, 2, 3])  # теперь работает


values_list = [5, "SUPER", False]
values_dict = {'a': 1, 'b': "str", 'c': True}


print_params(*values_list)
print_params(**values_dict)


values_list_2 = [35, "CLASS"]


print_params(*values_list_2, 42) # ok