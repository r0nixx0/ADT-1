# You can remove 'pass' if you written code in the function
# Do NOT use .append() or .pop() inside Push() and Pop() - move TopOfStack yourself.

# Exercise 1
Stack = [10, 20, 30, -1]
TopOfStack = -1
# Write code here to fill Stack with 10 elements, all -1


def IsEmpty():
    return TopOfStack == -1

    pass


def IsFull():
    return TopOfStack == 9
    pass


# Exercise 2
def Push(Item):
    global TopOfStack, Stack
    if IsFull():
        return False

    TopOfStack += 1
    Stack[TopOfStack]=Item
    return True
    pass


# Exercise 3
def Pop():
    global TopOfStack, Stack
    if IsEmpty():
        return -1
    Item=Stack[TopOfStack]
    TopOfStack=TopOfStack-1
    return Item

    pass
print(Pop())
print(TopOfStack)
print(Pop())
print(Pop())
print(Pop())

# Exercise 4
def Peek():
    # Write your code here
    pass


def Size():
    # Write your code here
    pass


# Exercise 5
def ReverseWord(Word):
    # Write your code here
    pass
