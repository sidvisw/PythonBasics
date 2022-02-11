# oh soldier prettify my folder
# path, dictionary file,format

# def soldier("C://","sid.txt","jpg")

# import os
# def soldier(directory,filename,Format):
#     os.chdir(directory)
#     f=open(filename)
#     content=f.read()
#     f.close()
#     print(content)
#     dir_list=os.listdir()
#     file_list=[item for item in dir_list if os.path.isfile(item)]
#     print(file_list)
#     for item in file_list:
#         if item not in content:
#             os.rename(item,item.capitalize())
#     i=1
#     for item in file_list:
#         if item.endswith(f".{Format}"):
#             os.rename(item,f"{str(i)}.{Format}")
#             i+=1
# directory=input("input the directory path you want to prettify=")
# filename=input("enter your file name which contains the file not to be prettified=")
# Format=input("enter your format of the file which you want to get numbered=")
# soldier(directory,filename,Format)
# print("your given directory successfully prettified")

import os
def soldier(path,file,format):
    os.chdir(path)
    i=1
    files=os.listdir(path)
    with open(file) as f:
        filelist=f.read().split('\n')
    for file in files:
        if file not in filelist:
            os.rename(file,file.capitalize())
        if os.path.splitext(file)[1]==format:
            os.rename(file,f"{i}{format}")
            i+=1
directory=input("input the directory path you want to prettify=")
filename=input("enter your file name which contains the file not to be prettified=")
Format=input("enter your format of the file which you want to get numbered=")
soldier(directory,filename,Format)
print("your given directory successfully prettified")

