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


list = []
n = int(input("enter the no. of test cases you want="))
print("Input your nos.....")
for i in range(n):
    list.append(int(input()))
for i in range(n):
    print(f"next palindrome for {list[i]} is {nextpalindrome(list[i])}")
