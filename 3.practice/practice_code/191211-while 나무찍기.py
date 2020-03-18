treeHit = int(input("나무 몇번찍었니?"))
mount = int(input("산 몇번탔니?"))
a = int(input("나무최대찍는 수"))
b = int(input("산타는 수"))
if treeHit < a :       # 10번 안에만 동작하게 함.
    while treeHit < a:     # 반복문도 10번 안에만 동작
        treeHit = treeHit + 1   
        print("나무를 %d번 찍었습니다."% treeHit)
        if treeHit == a :
            print("나무넘어감니다.")
            if mount < b : 
                while mount < b:
                    mount = mount + 1
                    print("%d번째 산타는중"% mount)
                    if mount == b :
                        print("다 탔다 겁나 힘들다.")
else :
    print("힘들어 고만해")
