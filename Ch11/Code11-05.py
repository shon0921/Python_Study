def findInsertIdx(ary, data) :
    findIdx = -1
    for i in range(0, len(ary)) :
        if (ary[i] > data) :
            findIdx = i
            break
    if findIdx == -1 :
        return len(ary)
    else :
        return findIdx

before = [188, 162, 168, 120, 50, 150, 177, 105]
after = []

print('정렬 전 -->', before)
for i in range(len(before)) :
    data = before[i]
    insPos = findInsertIdx(after, data)
    after.insert(insPos, data)
print('정렬 후 -->', after)
