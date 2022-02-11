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
    def __add__(self,other):
        return self.salary+other.salary
    def __truediv__(self,other):
        return self.salary/other.salary
    def __repr__(self):
        return f"Employee('{self.name}'',{self.salary},'{self.role}')"
    # def __str__(self):
    #     return f"the name is {self.name}. salary is {self.salary} and role is {self.role}"
emp1=Employee("harry",345,"programmer")
# emp2=Employee("rohan",85,"cleaner")
# print(emp1+emp2)
# print(emp1/emp2)
print(emp1) #or print(str(emp1))
print(repr(emp1))
print(str(emp1))