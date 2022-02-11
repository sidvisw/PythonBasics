import json
data='{"var1":"harry","var2":56}'
print(data)
# print(data['var1'])

parsed=json.loads(data)
print(parsed)
print(parsed['var1'])
print(type(parsed))

# task1-json.load?

data2={
    "channel_name":"codewithharry",
    "cars":['bmw','audi a8','ferrari'],
    "fridge":('roti',540),
    "isbad":False
}
jscomp=json.dumps(data2)
print(jscomp)

# task2-what is sort_key parameter in json.dumps()