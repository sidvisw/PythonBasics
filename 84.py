import random


def rohanMultiplication(n):
    lst = []
    k = random.randint(0, 9)
    for i in range(10):
        if i == k:
            lst.append(random.randint(n*i, n*(i+1)))
        else:
            lst.append(n*(i+1))
    return lst


def iscorrect(table, no):
    for i in range(10):
        if no*(i+1) != table[i]:
            return i
    return None


if __name__ == '__main__':
    n = int(input("enter the no. whose multiplication table you want="))
    table=rohanMultiplication(n)
    print(table)
    if iscorrect(table,n) == None:
        print("The multiplication table generated by rohan is correct")
    else:
        print(f"The multiplication table generated by rohan has an error at the {iscorrect(table,n)} index")
