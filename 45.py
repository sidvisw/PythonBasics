class Employee:
    no_of_leaves=8
    def __init__(self,aname,asalary,arole):
        self.name=aname
        self.salary=asalary
        self.role=arole
    def printdetails(self):
        return(f"the name is {self.name}. salary is {self.salary} and role is {self.role}")
    @classmethod
    def change_leaves(cls,newleaves):
        cls.no_of_leaves=newleaves
harry=Employee("harry",255,"instructor")
rohan=Employee("rohan",455,"student")
# Employee.no_of_leaves=89
# Employee.change_leaves(34)
harry.change_leaves(34)
print(harry.no_of_leaves)