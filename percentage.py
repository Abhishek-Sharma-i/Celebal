n = int(input("Enter the number of students:"))
student_marks = {}

for _ in range(n):
    data = input("Enter the name of student with their marks:").split()
    name = data[0]    
    marks = list(map(float, data[1:]))
    student_marks[name] = marks

query_name = input("Enter the name of students to query:")
average = sum(student_marks[query_name]) / len(student_marks[query_name])
print("{:.2f}".format(average))
