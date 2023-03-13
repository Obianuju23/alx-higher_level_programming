#!/usr/bin/python3
def no_c(my_string):

    new_str = ""
    for each_item in my_string:
        for i in each_item[:]:
            if i != 'c' and i != 'C':
                new_str += i
    return (new_str)
