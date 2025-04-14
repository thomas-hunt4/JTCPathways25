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

# iteration through a key
for key in student:
    print(key)

# to iterate and return keys and their values. 
for key, value in student.items():
    print(f"{key}: {value}")

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