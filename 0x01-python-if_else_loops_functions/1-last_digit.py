#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
 
last digit = abs(number) % 10
 
message = f"Last digit of {number} is {lastdigit}"

if lastdigit == 0:
         print(f"{message} and is 0")
elif lastdigit < 6 and lastdigit != 0:
         print(f"{message} and is less thsn 6 and not 0")
elif lastdigit > 5:
         print(f"{message} and is greater than 5")
