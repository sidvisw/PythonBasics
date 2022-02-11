# def searcher():
#     import time
#     # some 4 sec time cosuming task
#     book="this is a book on harry and code with harry and good"
#     time.sleep(4)
#     while True:
#         text=(yield)
#         if text in book:
#             print("your text is in the book")
#         else:
#             print("text is not in the book")
# search=searcher()
# print("search started")
# next(search)
# print("next method run")
# search.send("harry")
# search.close()
# search.send("harry")
# input("press any key")
# search.send("harry and")
# input("press any key")
# search.send("this is")
# input("press any key")
# search.send("joker")
# input("press any key")
# search.send("like this video")
def searcher():
    f=open("sid.txt")
    content=f.read()
    f.close()
    while True:
        text=(yield)
        if text in content:
            print("your text is in the book")
        else:
            print("text is not in the book")
search=searcher()
next(search)
string=input("enter the text you want to search=")
search.send(string)
search.close()