#1 Милі в кілометри km=mi/0,62137
def convert_kilometers(miles:float) -> float:
    if miles < 0:
        raise ValueError
    result = round(miles / 0.62137,2)
    return result

my_miles = 6
res = convert_kilometers(my_miles)
print(res)

#2
def get_plural(data) -> tuple:
    elements = sorted(set(data))
    return tuple(elements)

