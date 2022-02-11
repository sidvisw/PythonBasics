#list1=[["harry",1],["larry",2],["carry",6],["marie",250]]
#dict1=dict(list1)
#print(dict1)
#for item,lollypop in list1:
    #print(item,"and lolly is",lollypop)
#for item,lollypop in dict1.items():
    #print(item,"and lolly is",lollypop)
#for item in dict1:
    #print(item)
list1=["harry",56,"larry",2,4,7,8,"carry"]
#print(type(list1[1]))
for item in list1:
        if(str(item).isnumeric() and item>6):
            print(item)