# ls=[]
# for i in range(100):
#     if i%3==0:
#         ls.append(i)
# ls=[i for i in range(100) if i%3==0]
# print(ls)
# {0:"item0",1:"item1",....}
# dict1={i:f"item {i}" for i in range(1,10001) if i%100==0}
# print(dict1)
# dict1={i:f"item {i}" for i in range(5)}
# dict2={value:key for key,value in dict1.items()}
# print(dict1,"\n",dict2)
# dresses={dress for dress in ['dress1','dress2','dress1','dress2','dress1','dress2']}
# print(dresses)
# print(type(dresses))
# evens=(i for i in range(100) if i%2==0)
# print(type(evens))
# print(evens)
# print(evens.__next__())
# print(evens.__next__())
# print(evens.__next__())
# print(evens.__next__())
# for i in evens:
#     print(i)
lst=[]
n=int(input("enter the no of items you want="))
for i in range(n):
    lst.append(input(f"enter you item {i+1}="))
type=input("enter in which form you want to make comprehension=")
if(type=="list"):
    comp=[i for i in lst]
    print(comp)
elif(type=="dictionary"):
    comp={num:item for num in range(n) for item in lst}
    print(comp)
elif(type=="set"):
    comp={i for i in lst}
    print(comp)
else:
    print("invalid input")