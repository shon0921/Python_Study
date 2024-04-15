katok = ["다현","정연","쯔위","사나","지효"]

print(katok)
def insert_data(position, friend) :

    if position < 0 or position >len(katok) :
        print("데이터를 삽입할 범위를 벗어났습니다.")
        return

    katok.append(None)
    kLen=len(katok)

    for i in range(kLen-1,position,-1) :
        katok[i]=katok[i-1]
        katok[i-1]=None

    katok[position] =friend

while True :
    pos=int(input("삽입할 위치 --> "))
    data=input("추가할 데이터 -->")
    insert_data(pos,data)
    print(katok)


