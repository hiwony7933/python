marks = [90,25,67,45,80]
number = 0
average = sum(marks) / len(marks)
aa = len(marks)
bb = marks[:]
bb.sort()

for i in marks :
    number = number + 1
    if i >=60 :
        print("%d번 학생은 %d명 중에 %0.2f점 합격" % (number, aa, i))
    else :
        print("%d번 학생은 %0.2f점 불합격" % (number, i))
print(average)


# for mark in marks :
# number = number + 1
# if mark  60 : continue
# print("%d번 학생 축하해. 합격임" % number)
