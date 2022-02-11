# pickle
# requests module to download the iris dataset
import requests
import pickle

# pickling the iris ml data
# r=requests.get("https://archive.ics.uci.edu/ml/machine-learning-databases/iris/iris.data")
# data=r.text
# data=data.split("\n")
# data=[item.split(",") for item in data if len(item)!=0]
# f=open("iris.pkl","wb")
# pickle.dump(data,f)
# f.close()

f=open("iris.pkl",'rb')
data=pickle.load(f)
print(data)