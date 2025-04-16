# # Sets of students enrolled in each course
# course_a_students = {
#      "Alice", "Bob", "Charlie"
# }

# course_b_students = {
#      "Bob", "Diana", "Eve"
# }

# # TODO: Find students enrolled in both courses
# both_courses = course_a_students & course_b_students
# #  print(both_courses) # Replace with your code

# # TODO: Find students enrolled in either course
# either_course = course_a_students | course_b_students 
#  # Replace with your code

# # TODO: Find students enrolled in course A but not course B
# only_a = course_a_students - course_b_students  # Replace with your code

# # TODO: Find students enrolled in course B but not course A
# only_b = course_b_students - course_a_students
#  # Replace with your code

# # Print results
# print("Both courses:", both_courses)
# print("Either course:", either_course)
# print("Only in Course A:", only_a)
# print("Only in Course B:", only_b)

# tuple ****************************************************************************

# coordinates = {(0, 0): 'origin', (1, 0): 'unit x', (0,1): 'unit y'}
# print(coordinates[(0, 0)])

# def count_words(text):
#     words = text.lower().split()
#     word_count = {}
    
#     for word in words:
#         # Remove punctuation (simple approach)
#         word = word.strip('.,!?;:"\'()[]{}')
        
#         # Update count
#         if word in word_count:
#             word_count[word] += 1
#         else:
#             word_count[word] = 1
    
#     return word_count

# sample_text = "Python is amazing. Python is also easy to learn. Python is a versatile language."
# word_frequencies = count_words(sample_text)
# print(word_frequencies)

# # sample_text = "Python is amazing. Python is also easy to learn. Python is a versatile language."
# # word_freq = cour

# responses = [
#     "string", "something"
# ]

# uniq_resp = set(responses)
# print(f"Unique responses: {responses}")

# response_count = {}
# for answer in responses:
#     response_count[answer] = 

def group_by_domain(email_list):
    """
    Takes a list of email addresses and returns a dictionary
    where keys are domains and values are lists of usernames.
    """
    domain_dict = {  
        domain = emails.lower().split(@)
#     word_count = {}
    
#     for word in words:
#         # Remove punctuation (simple approach)
#         word = word.strip('.,!?;:"\'()[]{}')
        
    }

    # TODO: Fill in logic to populate domain_dict

    return domain_dict

print(group_by_domain)
# Example input (students can add their own)
emails = [
    "alice@gmail.com",
    "bob@yahoo.com",
    "carol@gmail.com",
    "dave@outlook.com"
]

# Call the function and print the result
result = group_by_domain(emails)
print(result)