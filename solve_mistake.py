# очікуваний результат у вигляді: My name is David, I am 14 years old👣

# example
# f = '\N{Footprints}'  # not informative naming, the correct code below
smile_footprint = '\N{Footprints}'

user_name = input('Please, enter your name >>> ')
user_age = input('Please, enter your age >>> ')
result = 'My name is ' + user_name + ', I am ' + user_age + ' years old' + smile_footprint

print(result)
