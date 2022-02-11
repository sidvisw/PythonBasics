f1=open("sid.txt")
try:
    f=open("does2.txt")
# except Exception as e:
#     print(e)
except EOFError as e:
    print("print EOFError aa gya h",e)
except IOError as e:
    print("print IOError aa gya h",e)
    
else:
    print("this will run only if except is not running")
finally:
    print("run this anyway...")
    # f.close()
    f1.close()
print("important stuff")