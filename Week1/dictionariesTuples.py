                # Basic structure of a dictionary. 


# student == var
# "name"  == key
# to right of : are values

student = {
    "name": "Alice",
    "age" : 20,
    "grade" : [85,90,88]
}

print(student)
# print(student("name"))
# print(student("grade"))

# alt method of dictionary creation using dict
contact = dict(name="Bob", phone="567-5309", email="bobiscool@bob.com")
print(contact)


# Better method in case a key value doesn't exist. 
print(student.get("name"))
print(student.get("grade"))

# adding a key to your dictionary
student["address"] = "123 Main St"
print(student)

# updating a value
student["age"] = 21
print(student)

# remove a key
del student["grade"]
print(student)

# remove a key alt
# grade = student.pop('grade')
print(student)

# iteration through a key
for key in student:
    print(key)

# return keys from dictionary
keys = student.keys()
print(keys)

# return keys and items from dictionary
items = student.items()
print(items)
print("*********TEST REF LINE**********")

# to iterate and return keys and their values. 
for key, value in student.items():
    print(f"{key}: {value}")

# to print keys only
for key in student:
    print(key)

# return a list of values from dictionary
for value in student.values():
    print(value)

# clear contents of a dictionary
student.clear()
print(student)

# adding keys and values from new dictionary
new_students = { "jeff": 27}
student.update(new_students)
print(student)



# ********************************SETS*******************************
# set does not hold duplicate values
empty_set = set[1]
print(empty_set)
print(type(empty_set))

# will not return the duplicate values
numbers = set({1, 2, 3, 4, 1, 3})
print(numbers)

# returns the string as individual char?
letters = set('hello')
print(letters)


# union*********************************
set_a = {1, 2, 3, 4, 5}
set_b = {4, 5, 6, 7, 8}

# joining multiple sets into one
union_set = set_a | set_b
print(f'Union: {union_set}')

# intersection
intersection_set = set_a & set_b
print(f'Intersection: {intersection_set}')

# the difference between two sets
difference_set = set_a - set_b
print(f'Difference A-b: {difference_set}')


symmetric_dif = set_a ^ set_b
print(f'Symmetric difference: {symmetric_dif}')

# adding to set
set_a.add(7)
print(set_a)

# add multiple items to a set
set_a.update([13, 9, 57])
print(set_a)

# remove an item from set  
set_a.remove(7)
print(set_a)

set_a.discard(9)
print(set_a)

# remove random element from set  
item = set_a.pop()
print(f'Popped: {item}')
print(union_set)

#                           Tuple
# A tuple is an ordered, immutable(it can not be changed) collection of items.
# Ideal for constant or unchanging data. Ensures integrity and prevents
#         accidental changes    

# Examples of a tuple
coordinates = (10, 20, 30)
print(coordinates)

colors = "red", "green", "blue"
print(colors)

# indexing with a tuple
print(coordinates[0])

# slicing with a tuple
print(coordinates[:2])

students = {
    "Alice": (20, "Math"),
    "Bob": (22, "Physics"),
    "Charlie": (19, "Biology")
}

for name, details in students.items():
    age, subject = details
    print(f"{name} is {age} years old and studies {subject}.")


# Tuple class
# 
# 
def get_user_info():
    name = "Alice"
    age = 30
    country = "USA"
    return name, age, country

user = get_user_info()
print(user)


name, age, country = get_user_info()
print(f"{name} is {age} and lives in {country}.")