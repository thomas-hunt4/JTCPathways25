# # Use and move lecture material to the appropriate folders from here




# mainmenu = ["*", "**", "***", "**", "*"]
# for index, mainmenu in enumerate(mainmenu, start = 1):
#     print(f"{index}.{mainmenu}")

# print(mainmenu)

# # # mainmenu = ["*", "**", "***", "**", "*"]
# # # for index, mainmenu in (mainmenu, start = 1):
# #     print(f"{index}.{mainmenu}")

# def greet_human(name):
#     print(f"Hello, {name}!")

# greet_human("Alice")

# def classify_person(name, age):
#     if age < 13:
#         print(f"{name},is a child.")
#     elif age >= 13 and age <= 19:
#         print(f"{name} is a teenager.") 
#     elif age >= 20 and age <= 64:
#         print(f"{name} is an adult.")
#     elif age >= 65:
#         print(f"{name} is a senior")
#     else:
#         print("Please make a valid entry")


# something is not working on my rewrite on this function. work on the age range formula
# def classify_person2(name, age):
#     if age < 13:
#         print(f"{name},is a child.")
#     elif 13 >= age <= 19:
#         print(f"{name} is a teenager.") 
#     elif age >= 20 and age <= 64:
#         print(f"{name} is an adult.")
#     elif age >= 65:
#         print(f"{name} is a senior")
#     else:
#         print("Please make a valid entry")      
    # """
    # Create a function that returns whether a person is a child, teenager, adult, or senior based on their age
    # Under 13: "[name] is a child."
    # 13-19: "[name] is a teenager."
    # 20-64: "[name] is an adult."
    # 65+: "[name] is a senior."
    # """
    # Your code here
#     pass

# # # Test cases
# classify_person2("Alex", 10)
# classify_person2("Jamie", 15)
# classify_person2("Taylor", 30)
# classify_person2("Morgan", 70)

def div_safely(a, b):
    if b != 0:
        return a/b
    else:
        return("Cannot divid by zero!")

result1 = div_safely(10, 2)

result2 = div_safely(5, 0)

def grade_score(score):
    if score >= 90:
        return "A"
    elif score >= 80:
        return "B"
    elif score >= 70:
        return "C"
    elif score >= 60:
        return "D"
    else:
        return "F"


print(f"Score 85: {grade_score(85)}")
print(f"Score 92: {grade_score(92)}")
print(f"Score 49: {grade_score(49)}")

def sum_list(numbers):
    total = 0
    for num in numbers:
        total += num
    return total

my_numbers = [1, 2, 3, 4, 5]
print(f'Sum of {my_numbers} is {sum_list(my_numbers)}')

def calculate_average(numbers):
    if not numbers:
        return 0
    total = sum_list(numbers)
    return total/len(numbers)

test_scores = [88, 92, 65, 78, 83]
print(f"Average score: {calculate_average(test_scores)}")