answer_li = []

f = open("D:/python/1000.txt", "r")
answer_li = f.readlines()
f.close()


for i in range(len(answer_li)) :
    answer_li[i] = answer_li[i].strip().replace(" ", "")

print(answer_li)

for i in range(len(answer_li)) :

    for j in answer_li :

        sum = answer_li[i] + str(j)

sum_li = list(sum)
print(sum_li)



