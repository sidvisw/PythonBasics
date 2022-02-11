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
    @classmethod
    def from_dash(cls,string):
        return cls(*string.split("-"))
    @staticmethod
    def printgood(string):
        print("this is good"+string)
        return 89
harry=Employee("harry",255,"instructor")
rohan=Employee("rohan",455,"student")
karan=Employee.from_dash("Karan-480-student")
print(karan.printgood("harry"))
print(Employee.printgood("rohan"))