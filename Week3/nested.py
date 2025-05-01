# ***************
# list as values within dictionary so that keys remain the same   

cart = {
    "fruits": ['mango', 'apples', 'oranges'],
    'vegetables': ['spinich', 'peas'],
    'grains': ['rice'],
    'other': []
                   
}

print(cart)

veggies = cart['vegetables']
print("egetables1in cart: veggies")


first_fruit = cart['fruits'][0]
print(first_fruit)

cart['vegetables'].append('bell peppers')
print('Updated vegetables:', cart['vegetables'])

# updating an item on list by calling the key and location
cart['fruits'] [0] = 'papayas'
print("update fruits:", cart['fruits'])    



# creating a new key and list   
cart['dairy'] = ['milk', 'cheese']

print('All fruits in cart:')

# for fruits in cart['fruits']:
#     print(f' - {fruits}')


# return every item on list by category

for category, items in cart.items():
    if isinstance(items, list):
        print(f'{category.title()}')
        for item in items:
            print(f'-{item}')
        else:
                print(f'{category.title()}:{items}')


# patricks recipe retrieval of dict in dict from in class lecture. 

# Real-World Example - Recipe Ingredients:
# A recipe with ingredients organized by category
# recipe = {
#     'name': 'Vegetable Stir Fry',
#     'prep_time': 15,
#     'cook_time': 10,
#     'servings': 4,
#     'ingredients': {
#         'proteins': ['tofu', 'cashews'],
#         'vegetables': ['bell pepper', 'broccoli', 'carrot', 'snow peas'],
#         'aromatics': ['garlic', 'ginger', 'green onion'],
#         'sauce': ['soy sauce', 'sesame oil', 'corn starch']
#     },
#     'steps': [
#         'Press and cube tofu',
#         'Chop all vegetables',
#         'Mix sauce ingredients',
#         'Stir-fry aromatics',
#         'Add vegetables and tofu',
#         'Add sauce and simmer'
#     ]
# }

# print(f'ingredients for {recipe['name']}(Serves{recipe['servings']})')
# for category, items in recipe['ingredients'].items():
#      print(f'{category.title()}')
#      for item in items:
#           print(f'- {item}')


# in class working with nested dictionaries
# ****************************************************************************************


# A nested dictionary of restaurants
# restaurants = {
#     'Amendolas': {
#         'address': '28 Lake St, Monroe, NY 10950',
#           'menu_url': 'https://www.amendolaspizzapasta.com/'
#     },
#     'LaVera Cucina': {
#         'address': '43 Hillside Terrace, Monroe, NY 10950',
#         'menu_url': 'https://www.veramonroe.com/'
#     }
# }
# print("Restaurant information:")
# print(restaurants)
# # Accessing Data in Nested Dictionaries:
# # Access information about a specific restaurant
# sri_info = restaurants['LaVera Cucina']
# print("LaVera Cucina info:", sri_info)
# # Access a specific piece of information
# el_basurero_address = restaurants['Amendolas']['address']
# print("Amendolas address:", el_basurero_address)
# # Using get() with a default value for safer access
# el_basurero_phone = restaurants.get('Amendolas', {}).get('phone', 'Not available')
# print("Amendolas phone:", el_basurero_phone)
# # Modifying Nested Dictionaries:
# # Add a new restaurant
# restaurants['Joes Pizza'] = {
#     'address': '7 Carmine St, New York, NY 10014',
#     'phone': '212-366-1182'
# }
# print("Added Joe's Pizza:", restaurants['Joes Pizza'])
# # Add a new field to an existing restaurant
# restaurants['Joes Pizza']['menu_url'] = 'http://www.joespizzanyc.com'
# print("Updated Joe's Pizza:", restaurants['Joes Pizza'])
# # Update an existing field
# restaurants['Joes Pizza']['menu_url'] = 'http://www.joespizzanyc.com/menu.php'
# # Remove a field
# restaurants['Joes Pizza'].pop('phone')
# print("Joe's Pizza after removing phone:", restaurants['Joes Pizza'])
# # Iterating Through Nested Dictionaries:
# # Print all restaurant information in a formatted way
# print("\nAll Restaurants:")
# for restaurant_name, details in restaurants.items():
#     print(f"\n{restaurant_name}:")
#     for key, value in details.items():
#         print(f"  {key}: {value}")
# # veramonroe.comveramonroe.com
# # La Vera Cucina - Italian American Restaurant - Monroe NY
# # La Vera Cucina located in Monroe NY serves the finest Italian American cuisine in the Hudson Valley


# *******************************************************************
# print('All restaurants:')
# for restaurant_name, details in restaurants.items():
#      print(f'{restaurant_name}')
#      for key, value in details.items():
#           print(f'{key}: {value}')


# Real-World Example - Product Inventory:
# A product inventory system
# inventory = {
#     'electronics': {
#         'smartphones': {
#             'iPhone 13': {'price': 799, 'stock': 15, 'colors': ['black', 'white', 'red']},
#             'Samsung Galaxy S21': {'price': 699, 'stock': 10, 'colors': ['black', 'silver']}
#         },
#         'laptops': {
#             'MacBook Pro': {'price': 1299, 'stock': 5, 'specs': {'ram': '16GB', 'storage': '512GB'}},
#             'Dell XPS': {'price': 999, 'stock': 8, 'specs': {'ram': '8GB', 'storage': '256GB'}}
#         }
#     },
#     'clothing': {
#         't-shirts': {
#             'Basic Tee': {'price': 19.99, 'stock': 50, 'sizes': ['S', 'M', 'L', 'XL']},
#             'Graphic Tee': {'price': 24.99, 'stock': 35, 'sizes': ['M', 'L']}
#         }
#     }
# }

# # Print all products with low stock (less than 10)
# print("\nLow Stock Items:")
# for category, subcategories in inventory.items():
#     for subcategory, products in subcategories.items():
#         for product, details in products.items():
#             if details['stock'] < 10:
#                 print(f"{category} - {subcategory} - {product}: Only {details['stock']} left!")



# # Start with this basic structure
# school = {
#     "Computer Science": {
#         "chair": "Dr. Jane Smith",
#         "courses": {
#             "CS101": {"name": "Intro to Programming", "instructor": "Dr. Brown", "credits": 3},
#             "CS201": {"name": "Data Structures", "instructor": "Dr. Green", "credits": 4}
#         }
#     },
#     "Mathematics": {
#         "chair": "Dr. Tom Johnson",
#         "courses": {
#             "MATH101": {"name": "Calculus I", "instructor": "Dr. White", "credits": 4},
#             "MATH205": {"name": "Linear Algebra", "instructor": "Dr. Brown", "credits": 3}
#         }
#     }
# }

# # Task 1: Add a new course "CS301: Database Systems" to Computer Science
# # taught by "Dr. Lee" with 4 credits
# # Your code here
# school['Computer Science']['courses'].append('CS301': 'name': 'Database Systems', 'instructor': 'Dr. Lee', 'credits' : 4 )
# print(school)


# Task 2: Find and print all courses taught by "Dr. Brown"
# Your code here

# Task 3: Print a formatted list of all departments and their courses
# Your code here


# dictionaries within a list****************************************************

# Live Coding Example - Basic List of Dictionaries:
# A list of user dictionaries
users = [
    {'username': 'ash', 'password': 'ilovepython', 'last_login': '9/28/2020'},
    {'username': 'aryn', 'password': 'ilovedictionaries'},
    {'username': 'yusuf', 'password': 'ilovejavascript', 'last_login': '9/26/2020'},
    {'username': 'paul', 'password': 'ilovegit'}
]

print("User accounts:")
print(users)

# Accessing Data in Lists of Dictionaries:
# Access a specific dictionary from the list
yusuf_account = users[2]
print("\nYusuf's account:", yusuf_account)

# Modifying Lists of Dictionaries:
# Add a new user to the list
users.append({'username': 'aeshna', 'password': 'ilovesublimetxt'})
print("\nAdded a new user:", users[-1])

# Modify an existing user's data
users[2]['verified_account'] = True
users[2]['password'] = 'iloveprogramming'
users[2].pop('last_login', None)
print("Modified Yusuf's account:", users[2])

# Iterating Through Lists of Dictionaries:
# Print all usernames
print("\nAll usernames:")
for user in users:
    print(user['username'])

# Convert all usernames to uppercase
for user in users:
    user['username'] = user['username'].upper()

print("\nUsernames after uppercase conversion:")
for user in users:
    print(user['username'])

# Print all users with a 'last_login' field
print("\nUsers with last login information:")
for user in users:
    if 'last_login' in user:
        print(f"{user['username']} last logged in on {user['last_login']}")







# ******************************************************************************************Line break************     
# Real-World Example - Task Management:
# A task management system
tasks = [
    {'id': 1, 'title': 'Finish project proposal', 'status': 'completed', 'assigned_to': 'Alice', 'due_date': '2025-04-01'},
    {'id': 2, 'title': 'Review code', 'status': 'in progress', 'assigned_to': 'Bob', 'due_date': '2025-04-10'},
    {'id': 3, 'title': 'Fix bugs', 'status': 'in progress', 'assigned_to': 'Alice', 'due_date': '2025-04-15'},
    {'id': 4, 'title': 'Deploy application', 'status': 'pending', 'assigned_to': 'Charlie', 'due_date': '2025-04-20'},
    {'id': 5, 'title': 'Write documentation', 'status': 'pending', 'assigned_to': 'Bob', 'due_date': '2025-04-25'}
]

# Find all tasks assigned to Alice
alice_tasks = [task for task in tasks if task['assigned_to'] == 'Alice']
print("\nAlice's tasks:")
for task in alice_tasks:
    print(f"- {task['title']} ({task['status']})")

# Count tasks by status
status_count = {}
for task in tasks:
    status = task['status']
    if status in status_count:
        status_count[status] += 1
    else:
        status_count[status] = 1

print("\nTask status summary:")
for status, count in status_count.items():
    print(f"{status}: {count} tasks")

# Find overdue tasks (assuming today is April 15, 2025)
today = '2025-04-15'
overdue_tasks = [task for task in tasks if task['status'] != 'completed' and task['due_date'] < today]
print("\nOverdue tasks:")
for task in overdue_tasks:
    print(f"- {task['title']} (Due: {task['due_date']}, Assigned to: {task['assigned_to']})")




alice_task = []
for task in tasks:
    if task ['assigned_to'] == "Alice":
        alice_task.append(task)

print("Alice's task: ")
for task in alice_task:
    print(f'- {task['title']}{task['status']}')













