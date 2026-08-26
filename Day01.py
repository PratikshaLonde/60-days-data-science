name = input("Enter your name: ")
age = int(input("Enter your age: "))
salary = float(input("Enter your salary: "))

yearly_salary = salary * 12

person = {
    "name": name,
    "age": age,
    "salary": salary,
    "yearly_salary": yearly_salary
}

print(person)
