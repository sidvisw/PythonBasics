import time
initial=time.time()
# print(initial)
k=0
while(k<4):
    print("this is harry bhai")
    time.sleep(2)
    k+=1
print("while loop ran in",time.time()-initial,"sec")
initial2=time.time()
for i in range(4):
    print("this is harry bhai")
print("for loop ran in",time.time()-initial2,"sec")

# localtime=time.asctime(time.localtime(time.time()))
# print(localtime)