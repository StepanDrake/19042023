cities_last_ten_years = set(input('Введіть міста в яких ви побували за минулі 10 років через пробіл>>>').title().split())
сities_you_wish_visit = set(input('Введіть міста в яких ви хочете побувати за наступні 10 років >>>').title().split())
like_cities = cities_last_ten_years.intersection(сities_you_wish_visit)
if like_cities:
    print('мабуть, вам дуже сподобалося в містах, які ви повторили>>>', like_cities)
else:
    print('Співпадіння відсутні')