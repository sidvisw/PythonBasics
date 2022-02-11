"""
mystr="sid is a good boy"
print(len(mystr))
print(mystr[0:16])
print(mystr[0:50])
print(mystr[0:5:2])
print(mystr[:5])
print(mystr[::])
print(mystr[0:])
print(mystr[-4:-2])
print(mystr[::-1])
print(mystr[::-2])
"""
mystr="sidisagoodboy123"
print(mystr.isalnum())
mystr="sid Is a good boy"
print(mystr.isalpha())
print(mystr.endswith("boy"))
print(mystr.count("o"))
print(mystr.capitalize())
print(mystr.find("is"))
print(mystr.lower())
print(mystr.upper())
print(mystr.replace("is","are"))  