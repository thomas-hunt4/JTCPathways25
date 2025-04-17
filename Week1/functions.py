# examples

def calc_area(length, width):
    area = length * width
    print(f"The area of a rectangle with length of {length} and width {width} is {area}.")
    if length == width:
        print("This is a square BRO!")
calc_area()

                    # default values for parameters
                    # ="second parameter default"

def greet_with_message(name, message="How are you today?"):
    print(f"Hello, {name}! {message}")

greet_with_message()

            # Functions with #Return values

def add_numbers(a,b):
    return a + b
sum_result = add_numbers(5,3)
print(f"The sum is:{sum_result}")

print(f'10 + 20 = {add_numbers(10, 20)}')