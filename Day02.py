def avg(marks):
    return sum(marks) / len(marks)

marks = []

for i in range(5):
    mark = float(input("Enter marks: "))
    marks.append(mark)

average = avg(marks)

if average >= 75:
    print("Average:", average)
    print("Distinction")

elif average >= 40:
    print("Average:", average)
    print("Pass")

else:
    print("Average:", average)
    print("Fail")
