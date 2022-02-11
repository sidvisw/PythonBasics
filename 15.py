"""operators in python
arithmetic operators
assignment operators
comparison operators
identity operators
membership operators
bitwise operators"""
#arithemetic operators
print("5+6 is",5+6)
print("5-6 is",5-6)
print("5*6 is",5*6)
print("5/6 is",5/6)
print("15//6 is",15//6)
print("5**3 is",5**3)
print("5%3 is",5%3)
#assignment operators
x=5
print(x)
x+=7 #x=x+7
print(x)
x/=7
print(x)
x-=7
print(x)
x%=7
print(x)
#comparizon operators
i=8
print(i==5)
print(i!=5)
print(i>5)
print(i>=5)
#logical operators
a=True
b=False
print(a and a)
print(a and b)
print(a or b)
print(b or b)
#identity operators
print(a is b)
print(a is not b)
print(5 is not 7)
#membership operators
list=[3,3,2,2,39,33,35,32]
print(32 in list)
print(324 not in list)
#bitwise operators
#0-00
#1-01
#2-10
#3-11
print(0&1)
print(0|1)
print(0|3)
print(0&2)