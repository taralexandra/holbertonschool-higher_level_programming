#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)

str = 'Last digit of'

# Obtenir le dernier chiffre de manière correcte
last = abs(number) % 10
if number < 0:
    last = -last

if last > 5:
    print(f'{str} {number} is {last} and is greater than 5')
elif last == 0:
    print(f'{str} {number} is {last} and is 0')
else:
    print(f'{str} {number} is {last} and is less than 6 and not 0')
