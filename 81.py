def ispalindrome(string):
    if string == string[::-1]:
        return True
    else:
        return False


def nextpalindrome(no):
    no += 1
    while not ispalindrome(str(no)):
        no = int(no)+1
    return no


if __name__ == '__main__':
    list = []
    n = int(input("enter the no. of elements in the list="))
    for i in range(n):
        list.append(int(input(f"Enter your list element {i+1} =")))
    # for i in range(n):
    #     if list[i] > 10:
    #         list[i] = nextpalindrome(list[i])
    # print("your modified list is", list)
    print(f"Output List: {[list[i] if list[i] < 10 else nextpalindrome(list[i]) for i in range(n)]}")
