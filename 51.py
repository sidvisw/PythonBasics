# public-
# protected-
# private-
class Employee:
    no_of_leaves=8
    _protec=9
    __private=98

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
emp=Employee("harry",343,"programmer")
print(emp._protec)
print(emp._Employee__private)
# print(emp.__private)