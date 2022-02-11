class Employee:
    def __init__(self,fname,lname) -> None:
        self.fname=fname
        self.lname=lname
        # self.email=f"{fname}.{lname}@codewithharry.com"
    def explain(self):
        return f"this employee is {self.fname} {self.lname}"
    @property
    def email(self):
        if self.fname==None or self.lname==None:
            return"Email is not set. Please set is using setter"
        return f"{self.fname}.{self.lname}@codewithharry.com"
    @email.setter
    def email(self,string):
        print("setting now...")
        names=string.split("@")[0]
        self.fname=names.split(".")[0]
        self.lname=names.split(".")[1]
    @email.deleter
    def email(self):
        self.fname=None
        self.lname=None
skillf=Employee("skill","f")
# print(skillf.email)
# print(type(skillf))
# print(id("this is a string"))
o="this is a string"
# print(dir(o))
# print(dir(skillf))
import inspect
print(inspect.getmembers(skillf))