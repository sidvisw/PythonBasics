n=int(input("enter the no. of apples provided to harry="))
mn=int(input("enter the lower limit of your range="))
mx=int(input("enter the upper limit of your range="))
if mx==mn:
    print("this is not a range and mx is equal to mn")
for i in range(mn,mx+1):
    if n%i==0:
        print(i,"is a divisor of",n)
    else:
        print(i,"is not a divisor of",n)