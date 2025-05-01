# import math

# print(f"math import test {math.pi}")

# import math as m

# print(f"this is math with an alias {m.pi}")






# math import use 


# print(dir(math))


# print(locals())

# import os
# ** get current working directory
# print(f"Current directory: {os.getcwd()}")

# **list files in the current directory
# print("Files in current directory:")
# for item in os.listdir('.'):

# **Check if a file exist   
# file_path = "mathOps.py"
# if os.path.exists(file_path):
#     print(f"{file_path}")

# import datetime
# # **current date and time
# now = datetime.datetime.now()
# print(f"Current date and time: {now}")

# # **format date as a string
# formatted_date = now.strftime(%Y-%m-%d %H:%M:%S)
# print(f"Formatted date:{formatted_date}")

# # **Calculate time difference
# future_date = datetime.datetime(2023, 12, 31)
# time_differece = future_date - now
# print(f"Days until December 31, 2026{time_differece.days}")


# import numpy as np

# array1 = np.array([1, 2, 3, 4, 5])












# print(f"math import test {math.pi}")

# import math as m

# print(f"this is math with an alias {m.pi}")



def calc_avg(numbers):
        for value in numbers:
    # if avg in calc_avg == 0:
    #     return "Nothing on list"
    # else:
            numbers = sum(calc_avg(value))/len(calc_avg(value))
            return numbers
    
print(calc_avg([8,8,8,10,6]))