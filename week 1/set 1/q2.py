#salary name index
names = []
salaries = []
while True:
    name = input("Enter a name (or 'End' to finish): ")
    if name == "End":
        break
    salary = float(input("Enter their salary: "))
    names.append(name)
    salaries.append(salary)

average_salary = sum(salaries) / len(salaries)
print("Average salary: ", average_salary)

max_salary_index = salaries.index(max(salaries))
min_salary_index = salaries.index(min(salaries))

print("Highest salary: ", names[max_salary_index], salaries[max_salary_index])
print("Lowest salary: ", names[min_salary_index], salaries[min_salary_index])
