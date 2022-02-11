import pickle

#pickling a python object
# cars=["audi","bmw","maruti suzuki","harryti tuzuki"]
# file="mycar.pkl"
# fileobj=open(file,'wb')
# pickle.dump(cars,fileobj)
# fileobj.close()

file="mycar.pkl"
fileobj=open(file,'rb')
mycar=pickle.load(fileobj)
print(mycar)
print(type(mycar))

#pickle.loads=?