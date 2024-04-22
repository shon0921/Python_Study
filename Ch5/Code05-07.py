class Node() :
    def __init__ (self):
        self.data = None
        self.link = None
        self.number = 0

def printNodes(start) :
    current = start
    if current == None :
        return
    print(current.data, end= ' ')
    while current.link != start :
        current = current.link
        print(current.data, end=' ')
    print()

def findNode(findData) :
    global memort, head, current, pred

    current = head
    if current.data == findData :
        return current
    while current.link != head :
        current = current.link
        if current.data == findData :
            return current
    return Node()


memory = []
head, current, pre = None, None, None
dataArray = ["다현", "정연", "쯔위", "사나", "지효"]

if __name__ == "__main__" :

    count = 0

    node = Node()
    node.data=dataArray[0]
    head = node
    node.link = head
    count = count + 1
    node.number = count
    memory.append(node)

    for data in dataArray[1:] :
        pre = node
        node = Node()
        node.data = data
        pre.link = node
        node.link = head
        count = count + 1
        node.number = count
        memory.append(node)

    printNodes(head)

    fNode = findNode("다현")
    print(fNode.number)

    fNode = findNode("쯔위")
    print(fNode.number)

    fNode = findNode("재남")
    print(fNode.number)
