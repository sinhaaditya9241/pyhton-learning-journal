student_marks = {"alice" : 75,
                 "bob" : 80,
                 "charlie" : 90,
                 "abhinav" : 85}

student_name = input('enter student name:') 

if student_name in student_marks:
    print(student_name, 'has scored', student_marks[student_name], 'marks')
else:
    print('student not found')

