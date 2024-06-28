import random

def isStackFull() :
    global SIZE, stack, top
    if (top >= SIZE-1) :
        return True
    else :
        return False

def isStackEmpty() :
    global SIZE, stack, top
    if (top == -1) :
        return True
    else :
        return False

def push(data) :
    global SIZE, stack, top
    if (isStackFull()) :
        return
    top += 1
    stack[top] = data

def pop() :
    global SIZE, stack, top
    if(isStackEmpty()) :
        return None
    data = stack[top]
    stack[top] = None
    top -= 1
    return data

def peek() :
    global SIZE, stack, top
    if (isStackEmpty()) :
        return None
    return stack[top]

SIZE = int(input("스택 크기를 입력하세요 ==> "))
stack = [None for _ in range(SIZE)]
top = -1
a = 0

if __name__=="__main__" :
 
    while (a<SIZE) :
        data = input("입력할 데이터 ==> ")
        push(data)
        print("스택 상태 : ", stack)
        a = a+1

    random.shuffle(stack)

    print("과자집에 가는길 : ", end = ' ')
    for stone in stack :
        push(stone)
        print(stone, "-->", end = ' ')
    print("과자집")

    print("우리집에 오는길 : ", end = ' ')
    while True :
        stone = pop()
        if stone == None :
            break
        print(stone, "-->", end = ' ')
    print("우리집")
