class Employee:
    no_of_leaves=8
    def __init__(self,aname,asalary,arole):
        self.name=aname
        self.salary=asalary
        self.role=arole
    def printdetails(self):
        return(f"the name is {self.name}. salary is {self.salary} and role is {self.role}")
harry=Employee("harry",455,"instructor")
# rohan=Employee()
# harry.name="harry"
# harry.salary=455
# harry.role="instructor"
# rohan.name="harry"
# rohan.salary=4554
# rohan.role="student"
# print(rohan.printdetails())
print(harry.printdetails())
print(harry.no_of_leaves)