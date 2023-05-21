import requests

url = 'https://dummyjson.com/users?limit=100'
responce = requests.get(url)
data = responce.json()

louisville_citizen = [user for user in data["users"] if user["address"].get("city", '') == "Louisville"]
men_with_brown_hair = [user["age"] for user in data["users"] if user["gender"] == "male" and user["hair"]["color"] == "Brown"]
if men_with_brown_hair:
    average_age_men_with_brown_hair = round(sum(men_with_brown_hair) / len(men_with_brown_hair),1)
    print("Середній вік чоловіків с коричневим волоссям:", average_age_men_with_brown_hair)
print("Список чоловіків с коричневим волоссям в місті Louisville:")
for person in louisville_citizen:
    print(person["firstName"], person["lastName"])