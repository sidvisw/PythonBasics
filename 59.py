"""
iterable-__iter__() or __getitem__()
iterartor-__next__()
iteration-
"""
# def gen(n):
#     for i in range(n):
#         yield i
# for i in range(780000000000):
#     print(i)
# g=gen(3)
# print(g)
# print(g.__next__())
# print(g.__next__())
# print(g.__next__())
# print(g.__next__())

# for i in g:
    # print(i)

# h="harry"
# h=546546
# ier=iter(h)
# print(ier.__next__())
# print(ier.__next__())
# print(ier.__next__())
# for c in h:
#     print(c)

def gen_fibo(n):
    f1=0
    f2=1
    if n==1:
        yield f1
    else:
        yield f1
        yield f2
        for i in range(n-2):
            yield f1+f2
            f2=f1+f2
            f1=f2-f1
g=gen_fibo(9)
# for i in g:
#     print(i)

def gen_fact(n):
    prod=1
    for i in range(n):
        prod*=(i+1)
        yield prod
for i in gen_fact(5):
    print(i)
