# This program calculates grades for different students
# Notice how similar code is copied and pasted multiple times
print("Welcome to the Student Grade Calculator")
# Calculate grades for student 1

student_data = {
    "Alex": [72,99,47],
    "Taylor":[8,6,7,5],
    "Jordan": [98,100,12,7,98,78],
}

def student_grade_cal(name):
    if name in student_data:
        student_scores = student_data[name]
    
        total = sum(student_scores)
        avg = total / len(student_scores)


        if avg >= 90:
            print("Grade: A")
        elif avg >= 80:
            print("Grade: B")
        elif avg >= 70:
            print("Grade: C")
        elif avg >= 60:
            print("Grade: D")
        else:
            print("Grade: F")
        print(f"Student: {name}")
        print(f"Scores: {student_scores}")
        print(f"Average: {avg}\n")
    else:
        print("Student not found.")

# for _ in range(n):
stud_name = input("Enter student name: ")
stud_score = input("Enter student scores: ")

student_data.update({stud_name, stud_score}) 

student_grade_cal("Taylor")
student_grade_cal("Alex")
student_grade_cal("Jordan")
student_grade_cal("Alysha")
# print(f"\nStudent: {name}")
# print(f"Scores: {student_scores}")
# print(f"Average: {avg}")
# Calculate grades for student 2 - same code copied!
# student2_name = "Taylor"
# student2_score1 = 92
# student2_score2 = 88
# student2_score3 = 95
# student2_total = student2_score1 + student2_score2 + student2_score3
# student2_average = student2_total / 3
# print(f"\nStudent: {student2_name}")
# print(f"Scores: {student2_score1}, {student2_score2}, {student2_score3}")
# print(f"Average: {student2_average}")
# if student2_average >= 90:
#     print("Grade: A")
# elif student2_average >= 80:
#     print("Grade: B")
# elif student2_average >= 70:
#     print("Grade: C")
# elif student2_average >= 60:
#     print("Grade: D")
# else:
#     print("Grade: F")
# Calculate grades for student 3 - same code copied again!
# student3_name = "Jordan"
# student3_score1 = 76
# student3_score2 = 82
# student3_score3 = 79
# student3_total = student3_score1 + student3_score2 + student3_score3
# student3_average = student3_total / 3
# print(f"\nStudent: {student3_name}")
# print(f"Scores: {student3_score1}, {student3_score2}, {student3_score3}")
# print(f"Average: {student3_average}")
# if student3_average >= 90:
#     print("Grade: A")
# elif student3_average >= 80:
#     print("Grade: B")
# elif student3_average >= 70:
#     print("Grade: C")
# elif student3_average >= 60:
#     print("Grade: D")
# else:
#     print("Grade: F")
# print("\nThank you for using the Student Grade Calculator!")