try:
    user_input=int(input("enter your input(age or year of birth):"))
except Exception as e:
    print("invalid input")
    exit()
user_input=str(user_input)
if len(user_input)==4:
    type="year of birth"
else:
    type="age"
user_input=int(user_input)
if type=="year of birth" and user_input>2021 or type=="age" and user_input<0:
    print("you are not yet born")
    exit()
elif type=="year of birth" and user_input<1821 or type=="age" and user_input>200:
    print("you seem to be the oldest person alive")
    exit()
elif type=="year of birth":
    print("you will be 100 year old in the year",user_input+100)
elif type=="age":
    print("you will be 100 year old in",100-user_input+2021)
ch=input("do you want to optionally enter an year to know your age at that time?(y/n):")
if ch=='y':
    year_input=int(input("enter your year input:"))
    if type=="year of birth":
        print("your age will be",year_input-user_input,"in the year",year_input)
    else:
        print("your age will be",year_input-2021+user_input,"int the year",year_input)