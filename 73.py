# a=input("what is your name=")
# b=input("how much do you earn")
# if int(b)==0:
#     raise ZeroDivisionError("B is 0 so stoping the program")
# if a.isnumeric():
#     raise Exception("numbers are not allowed")
# print(f"hello {a}")
# 1000 lines taking 1 hr

c=input("enter your name=")
try:
    print(a)
except Exception as e:
    if c=="harry":
        raise ValueError("harry is blocked he is not allowed")
    print("exception handled")