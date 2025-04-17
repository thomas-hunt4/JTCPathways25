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


for value in student:
    print(f"{value}")

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