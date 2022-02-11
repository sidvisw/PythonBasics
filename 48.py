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

class Programmer(Employee):
    no_of_holiday=56
    def __init__(self,aname,asalary,arole,languages):
        self.name=aname
        self.salary=asalary
        self.role=arole
        self.languages=languages
    def printprog(self):
        return(f"the programmers's name is {self.name}. salary is {self.salary} and role is {self.role}. the languages are {self.languages}")
harry=Employee("harry",255,"instructor")
rohan=Employee("rohan",455,"student")
shubham=Programmer("shubham",555,"programmer",["python"])
karan=Programmer("karan",777,"programmer",["cpp","python"])
print(karan.printprog())
print(karan.printdetails())
print(karan.no_of_holiday)