import random
def checkCommon(lst1,lst2):
    for i in lst1:
        for j in lst2:
            if i==j:
                return True
    return False
if __name__=='__main__':
    lst=[]
    n=int(input("enter the no. of friends="))
    for i in range(n):
        lst.append(input(f"enter your friend {i+1} name="))
    firstname=[]
    lastname=[]
    for i in range(n):
        firstname.append((lst[i].split(" "))[0])
        lastname.append((lst[i].split(" "))[1])
    funny_name=lst.copy()
    while checkCommon(funny_name,lst):
        funny_name=[]
        random1=random.randint(0,n-1)
        random2=random.randint(0,n-1)
        while random2==random1:
            random2=random.randint(0,n-1)
        lastname[random1],lastname[random2]=lastname[random2],lastname[random1]
        for i in range(n):
            funny_name.append(firstname[i]+" "+lastname[i])
    print(funny_name)
    
