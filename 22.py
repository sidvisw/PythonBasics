# pattern printing
# input=interger n
# boolean=True or False
# True
# *
# **
# ***
# ****
# False
# ****
# ***
# **
# *
n=int(input("enter n="))
m=n
cond=int(input("enter true(1) or false(0)="))
while(n!=0):
    if(cond):
        print((m-n+1)*"*")
    else:
        print(n*"*")
    n-=1
        