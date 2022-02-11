 #snake water gun
import random
d={"s":"snake","w":"water","g":"gun"}
your_score=0
comp_score=0
n=10
def generate_rand():
    lst=["s","w","g"]
    return random.choice(lst)
while n!=0:
    n-=1
    comp_choice=generate_rand()
    your_choice=input("press\ns-snake\nw-water\ng-gun\nenter ur choice=")
    if your_choice=="s":
        if comp_choice=="w":your_score+=1
        elif comp_choice=="g":comp_score+=1
    elif your_choice=="w":
        if comp_choice=="g":your_score+=1
        elif comp_choice=="s":comp_score+=1
    elif your_choice=="g":
        if comp_choice=="s":your_score+=1
        elif comp_choice=="w":comp_score+=1
    print("the choice of computer was",d[comp_choice])
    print("ur score=",your_score,"computer score=",comp_score)
if comp_score>your_score:print("u lose better luck next time")
elif your_score>comp_score:print("u won congrats")
else:print("game tie")