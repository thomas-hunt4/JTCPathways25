# # **********w1d4 class notes******************

# # Syntax errors
# # mostly caught bu IDE

# # RuntimeError
# # usually seen in terminal
# # ******example= unassigned variable

# # logic errors
# # harder to find, must check the code   


# # TLE error   Time Limit Exceeded error   


# dict = {
#     "name": "Jeremy",
#     "age" : 28
# }

# # dict['fname']
# # **********produces KeyError because key does not exist. ***********


# print(dict)


# # list = [1, 2, 3]

# # list[4]  ****out of range*****index error*****

# inventory = ["beer", "chorizo", "hot sauce", "pan"]

# order_1 = ["beer", "pan"]

# def check_order(order):
#     if len(order) == 0:
#         return False
#     for item in order:
#         print("item in order, {item}")
#         if item not in inventory:
#             return False

#     return True
    
# order_1 = ["beer", "bob"]
        
# print(check_order(order_1))

# # **********************Try/Except***************************
# # Handle potential errors gracefully
# # could be in the form of a message or prompt to a user

# inventory_2 = {
#     1: "apple",
#     2: "banana",
#     3: "orange",
#     4: "grape"
# }

# try:
#     user_input = input("Enter an item number (1-4)")
#     order_number = int(user_input)
# except Exception as e:
#     print("Please make a valid entry")

# else:
#     print("Thank you for shopping with us!!")
# finally:
#     print("Bye")
   

# print(inventory_2(order_number))



def divide_inputs(input1, input2):
    num1 = float(input1)
    num2 = float(input2)
    return num1 / num2
       


def get_inputs():
    try:
        input1 = input("Enter the first number: ")
        input2 = input("Enter the second number: ")
        result = divide_inputs(input1, input2)
        print(result)
    # except ValueError as e:
    #     print("Please enter a numeric value")
    except ZeroDivisionError as z:
         print("Can not divide by zero")
    except Exception as e:
        print("Please enter valid response")
    

get_inputs()


# password conditions*****************************
# 8 char
# contain at least one uppercase letter
# contain at least one lowercase letter
# contain at least one number

class passwordvalidationerror(Exception):
    pass

try:
    user_1 = input("Enter a password: ")
    if len(user_1) < 8:
        raise passwordvalidationerror("Password must be more than 8 characters")
except passwordvalidationerror as e:
    print(e)

    hasUppercase = False
    for character in user_1:
        if character.isupper:
            hasUppercase = True
    if not hasUppercase:
        raise passwordvalidationerror("You need an uppercase character")
      
    hasLowercase = False
    for character in user_1:
        if character.isupper:
            hasLowercase = True
    if not hasLowercase:
        raise passwordvalidationerror("You need an uppercase character")   

    hasNumber = False
    for character in user_1:
        if character.isdigit:
            hasNumber = True
    if not hasNumber:
        raise passwordvalidationerror("Please include a number")   

except passwordvalidationerror as e:
    print("")        




print(user_1)