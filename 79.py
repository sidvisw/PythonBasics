list=[]
i=0
ch='y'
while ch=='y':
    list.append(input(f"enter the list item no {i+1}="))
    i+=1
    ch=input("do you wnat to continue adding?(y/n)=")
list_temp=list.copy()
list.reverse()
print(list)
l1=list_temp[::-1]
print(l1)
for i in range(len(list_temp)//2):
    list_temp[i],list_temp[len(list_temp)-i-1]=list_temp[len(list_temp)-i-1],list_temp[i]
print(list_temp)
if list==l1 and l1==list_temp:
    print("All three methods give the same results!")