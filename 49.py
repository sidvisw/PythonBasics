class Employee:
    no_of_leaves=8
    var=8
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
class Player:
    no_of_games=4
    var=9
    def __init__(self,name,game) -> None:
        self.name=name
        self.game=game
    def printdetails(self):
        return(f"the name is {self.name}. game is {self.game}")
class CoolProgrammer(Employee,Player):
    language="c++"
    # var=10
    def printlanguage(self):
        print(self.language)
harry=Employee("harry",255,"instructor")
rohan=Employee("rohan",455,"student")
shubham=Player("shubham",["cricket"])
karan=CoolProgrammer("karan",8990,"CoolProgrammer")
det=karan.printdetails()
karan.printlanguage()
print(det)
print(karan.var)