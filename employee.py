employee_salaries = {}

while True:
    name = input("Enter employee name (or 'no' to stop): ")
    if name.lower() == 'no':
        break
    salary = float(input("Enter employee salary: "))
    employee_salaries[name] = salary

print("Employee salaries:", employee_salaries)
