# def function_name_print(a,b,c,d,e):
#     print(a,b,c,d,e)

def funargs(normal,*args,**kwargs):
    print(normal)
    # print(type(args))
    # print(args[0])
    for item in args:
        print(item)
    print("now i would like to introduce yout o some of our heros")
    for key,value in kwargs.items():
        print(f"{key} is a {value}")
# def funargs(*args,normal):
#     print(normal)
#     # print(type(args))
#     # print(args[0])
#     for item in args:
#         print(item)
# function_name_print("harry","rohan","hammad","skillf","shivam")
har=["harry","rohan","hammad","skillf","shivam","the programmer"]
normal="i am a normal argument and the students are:"
kw={"rohan":"monitor","harry":"fitness instructor","the programmer":"coordinator","shivam":"cook"}
funargs(normal,*har,**kw)
funargs(normal)
# funargs(*har,normal)