#dictionary is key value pair
d1={}
#print(type(d1))
d2={"harry":"burger","rohan":"fish","rohit":"roti","shubham":{"b":"maggi","l":"roti","d":"chicken"}}
#print(d2)
#print(d2["harry"])
#print(d2["shubham"]) 
#print(d2["shubham"]["b"])
#d2["ankit"]="junk food"
#d2[420]="kebabs"
#print(d2)
#del d2[420]
#d3=d2
#del d3["harry"]
#print(d2)
#d3=d2.copy()
#del d3["harry"]
#print(d2)
# print(d2.get("harry"))
d2.update({"leena":"toffee"})
print(d2)
print(d2.keys())
print(d2.items())
