#Task10
students_last_name : str = input('Введіть прізвища учнів: ')
students_name_list : list = students_last_name.split(' ')
final_list : list = []
for element in students_name_list:
    element_copy=element.capitalize()
    final_list.append(element_copy)
final_list.sort()
for element in final_list:
    print(element)
