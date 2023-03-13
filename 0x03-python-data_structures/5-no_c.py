#!/usr/bin/python3
def no_c(my_string):
    new_string = ""

    for element in my_string:
        for i in element[:]:
            if i != 'c' and i != 'C':
                new_string = new_string + i
    return (new_string)
