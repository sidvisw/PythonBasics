a=9
b=8
c=sum((a,b)) #built in function
print(c)

def function1(a,b):
    print("hello u r in func 1",a+b)
function1(5,7)
def function2(a,b):
    """this is a func which will calculate avg of 2 nos
    this func doesnt work for 3 nos"""
    avg=(a+b)/2
    #print(avg)
    return avg
v=function2(5,7)
print(v)
print(function2.__doc__)