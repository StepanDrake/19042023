#1
def anekdoti(x):
    if x == 1:
        return 'Раніше в школі вчили читати і писати, а тепер в школі перевіряють, як дітей всьому цьому навчили вдома'
    elif x == 2:
        return  'На недільну рибалку запрошуються всі ентузіасти цієї справи. Цієї справи брати по дві пляшки на людину.'
    else:
        return  'Вночі прийшов кіт і скромно ліг у мене в ногах. А під ранок в ногах у кота спав вже я.'
print(anekdoti(2))
#2
def calculate_perimetr(length, width):
    return 2.0 * (length+width)
print(calculate_perimetr(8,7))
#3
def remove_chars_from_target(target_string, remove_string):
    for char in remove_string:
        target_string = target_string.replace(char.lower(), '').replace(char.upper(), '')
    return target_string
target_string = 'хижак'
remove_string = 'вікно'
cleaned_string = remove_chars_from_target(target_string, remove_string)
print(cleaned_string)
def remove_chars_from_target(target_string, remove_string):
    cleaned_string = ""
    for char in target_string:
        if char not in remove_string:
            cleaned_string += char
    return cleaned_string
target_string = 'вОно'
remove_string = 'вікно'
cleaned_string = remove_chars_from_target(target_string, remove_string)
print(cleaned_string)