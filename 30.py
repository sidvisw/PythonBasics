# f strings
import math
me="harry"
a1=3
# a="this is %s %s"%(me,a1)
# a="this is {} {}"
# a="this is {1} {0}"
# b=a.format(me,a1)
# print(b)
a=f"this is {me} {a1} {4*65} {math.cos(65)}"
print(a)