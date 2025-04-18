

# def calc_avg(numbers):
#     return sum(numbers)/len(numbers)    
    



# print(calc_avg([8,8,8,10,6]))

# *********************************line break**********************

# def count_words(text):
#     word = text.lower().split()
#     word_count = {}

#     for word in sample_text:
#         word = word.strip('.,!?;:"\'()[]{}')

#         if word in word_count:
#             word_count[word] += 1
    
#     return word_count


# sample_text = "Python is amazing. Python is also easy to learn. Python is a versatile language."
# word_frequencies = count_words(sample_text)
# print(word_frequencies)

# ********************line break*****************


# def divide(a, b):
#     if b == 0:
#         return "Can not divide by zero"
#     return a / b


# ***********line break*****************

def count_occurrences(count_list) -> dict:
    my_list = { 

    }

    for val in count_list:
        if val in my_list:
            my_list =+ 1
    else:
            my_list = 1
    return my_list

print(count_occurrences([1, 2, 3, 1, 2, 1]))