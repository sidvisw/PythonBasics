"""
grocery=["harpic","vim bar","deodrant","lollypop",56]
print(grocery)
print(grocery[3])
nos=[2,7,9,11,3]
nos.sort()
print(nos)
nos.reverse()
print(nos)
print(nos[:5])
print(nos[1:])
print(nos)
print(nos[::2])
print(nos[1:5:-3])
print(max(nos))
print(min(nos))
nos.append(7)
print(nos)
nos.insert(1,67)
print(nos)
nos.remove(9)
print(nos)
nos.pop()
print(nos)
"""
#nos=[2,7,9,11,3]
#nos[1]=98
#print(nos)
#mutable-can change(list)
#immutable-cant change(tuple)
tp=(1,2,3)
#tp[1]=8
print(tp)
tp2=(1,)
print(tp2)
a=1
b=8
#temp=a
#a=b
#b=temp
a,b=b,a
print(a,b)