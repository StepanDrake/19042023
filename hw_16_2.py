def get_month():
    month = [
        'Cічень',
        'Лютий',
        'Березень',
        'Квітень',
        'Травень',
        'Червень',
        'Липень',
        'Серпень',
        'Вересень',
        'Жовтень',
        'Листопад',
        'Грудень'
    ]

    while True:
        for elements in month:
            yield elements

generetor = get_month()
print(next(generetor))
print(next(generetor))
print(next(generetor))
print(next(generetor))
print(next(generetor))
print(next(generetor))
print(next(generetor))
print(next(generetor))
print(next(generetor))
print(next(generetor))
print(next(generetor))
print(next(generetor))
print(next(generetor))
