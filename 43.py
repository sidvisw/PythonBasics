class Employee:
    no_of_leaves=8
    pass
harry=Employee()
rohan=Employee()
harry.name="harry"
harry.salary=455
harry.role="instructor"
rohan.name="harry"
rohan.salary=4554
rohan.role="student"
print(rohan.name)
print(harry.salary)
# print(harry.no_of_leaves)
print(Employee.no_of_leaves)
# Employee.no_of_leaves=9
print(rohan.__dict__)
print(Employee.__dict__)
rohan.no_of_leaves=9
print(rohan.__dict__)
print(Employee.__dict__)
print(rohan.no_of_leaves)
Employee.no_of_leaves=9
print(Employee.no_of_leaves)