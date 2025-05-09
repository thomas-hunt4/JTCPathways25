

dictionary_is_key_value_pairs = {
    'Name': 'Alice',
    'Age': 20,
    'Major': 'Computer Science',
    'Grades': [89, 72, 98, 92]

}



def dictionaryfunction():
    return dictionary_is_key_value_pairs


# print(dictionary_is_key_value_pairs['Name'])

# print(dictionary_is_key_value_pairs['Grades'])

dictionary_is_key_value_pairs['GPA'] = {'Year 1': 3.8, 'Year 2': 3.6}
print(dictionary_is_key_value_pairs)

print(dictionary_is_key_value_pairs['GPA']['Year 2'])
# print(dictionary_is_key_value_pairs['Grades'][2])
# print(dictionary_is_key_value_pairs['Grades'][:])

new_meas = {'Favorite Taco': 'Lengua', 'Tacos per sitting': 9}
dictionary_is_key_value_pairs.update(new_meas)

print(dictionary_is_key_value_pairs)

# for value in dictionary_is_key_value_pairs.values():
#     print(value)

# for key, value in dictionary_is_key_value_pairs.items():
#     print(key, value)

# for key in dictionary_is_key_value_pairs:
#     print(key)

day = int(input("Please select option 1-7: "))

match day:
    case 1:
        dictionaryfunction()
    case 2:
        print('Tuesday')
    case 3:
        print('Wednesday')
    case 4:
        print('Thursday')
    case 5:
        print('Friday')
    case 6:
        print('Saturday')
    case 7:
        print('Sunday')
    