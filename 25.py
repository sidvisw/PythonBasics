#health management sytem
# 3 clients-harry,rohan,hammad

def getdate():
    import datetime
    return datetime.datetime.now()
# total 6 files
# write a func that when executed takes input client name
# one more func to retrieve excercise or food for any client
def Read(f):
    str1=f.read()
    print(str1)
def Write(f):
    str1=input("Enter ur entry=")
    f.write("[")
    f.write(str(getdate()))
    f.write("]")
    f.write(" ")
    f.write(str1)
    f.write("\n")
ch="y"
while ch=="y":
    pchoice=int(input("enter ur choice:\n1-harry\n2-rohan\n3-hammad\n"))
    if(pchoice==1):
        fchoice=int(input("what do u wanna read/write\n1-excercise\n2-diet\n"))
        if fchoice==1:
            choice=int(input("what do u wanna do\n1-read\n2-write\n"))
            if choice==1:
                f11=open("f11.txt")
                Read(f11)
                f11.close()
            else:
                f11=open("f11.txt","a")
                Write(f11)
                f11.close()
        else:
            choice=int(input("what do u wanna do\n1-read\n2-write\n"))
            if choice==1:
                f12=open("f12.txt")
                Read(f12)
                f12.close()
            else:
                f12=open("f12.txt","a")
                Write(f12)
                f12.close()
    elif(pchoice==2):
        fchoice=int(input("what do u wanna read/write\n1-excercise\n2-diet\n"))
        if fchoice==1:
            choice=int(input("what do u wanna do\n1-read\n2-write\n"))
            if choice==1:
                f21=open("f21.txt")
                Read(f21)
                f21.close()
            else:
                f21=open("f21.txt","a")
                Write(f21)
                f21.close()
        else:
            choice=int(input("what do u wanna do\n1-read\n2-write\n"))
            if choice==1:
                f22=open("f22.txt")
                Read(f22)
                f22.close()
            else:
                f22=open("f22.txt","a")
                Write(f22)
                f22.close()
    else:
        fchoice=int(input("what do u wanna read/write\n1-excercise\n2-diet\n"))
        if fchoice==1:
            choice=int(input("what do u wanna do\n1-read\n2-write\n"))
            if choice==1:
                f31=open("f31.txt")
                Read(f31)
                f31.close()
            else:
                f31=open("f31.txt","a")
                Write(f31)
                f31.close()
        else:
            choice=int(input("what do u wanna do\n1-read\n2-write\n"))
            if choice==1:
                f32=open("f32.txt")
                Read(f32)
                f32.close()
            else:
                f32=open("f32.txt","a")
                Write(f32)
                f32.close()
    ch=input("Do u want to continue?=")