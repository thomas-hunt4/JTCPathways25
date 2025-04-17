
'''
bike = ['honda', 'suzuki', 'yamaha', 'kawasaki', 'ducati', 'harley']
for bike in bike:
    print(bike)

for bike in range(3):
    if bike == input("Enter bike name"):
        print(bike)
    else:
        print("not a bike")    
'''

'''
fridge = ['milk', 'eggs', 'cheese', 'butter']
userinput = input("What we got to eat?")
infridge = False
for item in fridge:
    if item == userinput:
        infridge == True
        break

    if item == userinput:
    print("We already have that")
        
    else:
        print("add this to list")

'''


'''
user_input = ''
while user_input.lower() != "exit":
    user_input = input("Type something (or 'exit to quit): ")
    if user_input.lower() != "exit":
        print("You typed:", user_input)
print("Goodbye!")
 

'''

toDo = []
prompt = "Enter a task to add to your to-do list, or enter 'quit' to exit "
userInput = input(prompt)
print(userInput)
while userInput != "quit":
    toDo.append(userInput)
    userInput = input(prompt)
    for userInput in toDo:
        if userInput == "":
            toDo.remove
    print ("Current to-do list: ", toDo)
    print(userInput)
print("Thank you for adding to your list", toDo)