import csv

grades = []

with open("students.csv", "r") as file:
    data = csv.DictReader(file)
    for row in data:
        grades.append(row["Grade"])

frequency = {}

for grade in grades:
    frequency[grade] = frequency.get(grade, 0) + 1

with open("summary.txt", "w") as file:
    file.write("Grade Frequency\n")
    for grade, count in frequency.items():
        file.write(f"{grade}: {count}\n")

print("Summary created successfully!")