a=int(input("no1="))
b=int(input("no2="))
operator=input("operator=")
if(operator=="+"):
    if(a==56 and b==9 or a==9 and b==56):
        print("ans= 77")
    else:
        print("ans=",a+b)
elif(operator=="-"):
    print("ans=",a-b)
elif(operator=="*"):
    if(a==45 and b==3 or a==3 and b==45):
        print("ans= 555")
    else:
        print("ans=",a*b)
elif(operator=="/"):
    if(a==56 and b==6):
        print("ans= 4")
    else:
        print("ans=",a/b)