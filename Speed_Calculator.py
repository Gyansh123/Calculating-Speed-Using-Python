import math as math
import numpy as np
import matplotlib as mat

distance = float(input("Enter distance "))
time = float(input("Enter time "))

def calculate_speed(dis, ti):
    if dis == 0 and ti == 0:
        return "Error: Both distance and time cannot be zero."
    elif dis < 0 and ti < 0:
        return "Error: Distance and time cannot be negative."
    elif math.isnan(dis) and math.isnan(ti):
        return "Error: Distance and time cannot be NaN (Not a Number)."
    else:
        speed = dis / ti
        return round(speed, 2)

speed_value = calculate_speed(distance, time)
print("Speed = " + str(speed_value) + " distance_unit/time_unit")


# print("Note if this is in m/s units then comprehension is down below.")
#
# if 0 < speed_value < 20:
#     print("Speed is slow")
# elif 20 <= speed_value <= 50:
#      print("Speed is moderate")
