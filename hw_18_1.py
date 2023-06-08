import csv

with open("airport-codes_csv.csv", mode="r", encoding="utf-8") as file:
    reader = csv.DictReader(file, delimiter=';')
    for elements in reader:
        air = elements['iso_country']
        if air == "UA":
            print(elements["name"])