# l=10 #global variable

# def function1(n):
#     # l=5 #local variable
#     m=8 #local variable
#     global l
#     l=l+45
#     print(l,m)
#     print(n,"i have printed")

# function1("this is me")
# # print(m)
# print(l)


def harry():
    x=20
    def rohan():
        global x
        x=88
    print("before calling rohan()",x)
    rohan()
    print("after calling rohan()",x)
harry()
print(x)