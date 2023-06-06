import csv

with open("airport-codes_csv.csv", mode="r", encoding="utf-8") as file:
    reader = csv.DictReader(file, fieldnames=['iso_country = UA'], delimiter=';')
    for elements in reader:
        print(elements)
