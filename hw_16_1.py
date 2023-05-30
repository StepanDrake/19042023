def get_positiv_number(number):
    if number < 0:
        raise ValueError
    return [element for element in range(number, number+10)]
number = 1
number_list = get_positiv_number(number)
print(number_list)

number = 5
number_list = get_positiv_number(number)
print(number_list)
