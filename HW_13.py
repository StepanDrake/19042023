import requests

url = 'https://script.googleusercontent.com/macros/echo?user_content_key=On0P9IR4A5N7lFjkszgXCBTd0UjH3LsSWfI1SmE4SoA41o8HGhdc_mBaBIxBWoiFZ7UR0uhml9L1Esy8fbUYBOxzhY7zPtBHm5_BxDlH2jW0nuo2oDemN9CCS2h10ox_1xSncGQajx_ryfhECjZEnKnxYUmajR99tdeTKUMfF5kXcilO9Q9VB7NtnhLoC8RaLYiDh3UbhjvRxy7I1lbiKQj5tO1-L1-16c5D1UIsfMPeZ4cL2809Cdz9Jw9Md8uu&lib=MvxnxfSPAsJ2o_5n6Ngcd7MGIhzuPuY7m'
response = requests.get(url)
inner_data = response.json()['data']

total_cost = 0
gluten_free_cost = 0

for product_data in inner_data:
    print(product_data)
    price = product_data['price']
    residue = product_data['residue']
    contains_gluten = product_data['contains_gluten']
    total_cost +=residue * price
    if not contains_gluten:
        gluten_free_cost +=residue * price
print('Загальна вартість товарів:', total_cost)
print('Вартість товарів без глютену:' ,gluten_free_cost)