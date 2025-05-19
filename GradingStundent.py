
def gradingStudents(grades):
    # Write your code here
    newGrade = []
    for i in grades:
        if i >= 38 and i % 5 >= 3:
            i += 5 - i % 5
            newGrade.append(i)
        else:
            newGrade.append(i)
    print(list(newGrade))

gradingStudents([73, 67, 38, 33])

