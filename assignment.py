# You can remove 'pass' if you written code in the function
# Do NOT use .append() or .pop() inside Push() and Pop() - move TopOfStack yourself.

# Exercise 1
Stack=[-1]*10
TopOfStack=-1

def IsEmpty():
    return TopOfStack==-1

def IsFull():
    return TopOfStack==9

def Push(Item):
    global TopOfStack,Stack
    if IsFull():
        return False
    TopOfStack+=1
    Stack[TopOfStack]=Item
    return True

def Pop():
    global TopOfStack,Stack
    if IsEmpty():
        return -1
    Item=Stack[TopOfStack]
    TopOfStack=TopOfStack-1
    return Item

def Peek():
    if IsEmpty():
        return -1
    return Stack[TopOfStack]

def Size():
    return TopOfStack+1

def ReverseWord(Word):
    global TopOfStack,Stack
    TopOfStack=-1
    for char in Word:
        Push(char)
    reversed_word=""
    while not IsEmpty():
        reversed_word+=Pop()
    return reversed_word
