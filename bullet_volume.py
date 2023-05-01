import math


PI = math.pi
radius = float(input('Please, enter radius >>> '))
bullet_volume = round((4/3)*PI*pow(radius, 3),2)

print('Bullet volume =', bullet_volume)
