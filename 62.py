import time
from functools import cache, lru_cache
cache_num=int(input("enter the memory you want to cache="))
@lru_cache(maxsize=cache_num)
def some_work(n):
    # some task taking n second
    time.sleep(n)
    return n
# if __name__=="__main__":
#     print("now running some work")
#     some_work(3)
#     some_work(1)
#     some_work(6)
#     some_work(9)
#     print("done...calling again")
#     input()
#     some_work(3)
#     print("called again")
print("now running some work")
some_work(3)
some_work(1)
some_work(6)
some_work(9)
print("done...calling again")
input()
some_work(3)
print("called again")