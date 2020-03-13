
import random

jockbo_goang_top = [3, 8]   # 삼팔광땡 족보
jockbo_goang = [1, 3, 8]    # 광땡 족보
jockbo_ddang = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10] # 땡 족보
jockbo_ali = [1, 2, -1, -2]
jockbo_docksa = [1, 4, -1, -4]
jockbo_gubbing = [1, 9, -1, -9]
jockbo_jangbbing = [1, 10, -1, -10]
jockbo_seluk = [4, 6, -4, -6]

def jockbo_goang_top_def(first, second) :
    if first in jockbo_goang_top and second in jockbo_goang_top :
        print("천하무적%s %s 광땡 떴다 족보!" % (PC_first_abs, PC_second_abs))
    return

def jockbo_kabo_def(first, second):
    if (first + second) == 9 :
        print("%s %s 갑오 족보!" % (PC_first_abs, PC_second_abs))
    return



f = open("D:\python\Sudda/answer.txt", "r")

answer_li =f.readlines()

for i in range(len(answer_li)) :
    answer_li[i] = answer_li[i].strip().replace(" ", "")

PC_first_num = random.choice(answer_li)

while True :    # first 카드와 second 카드의 중복 제외 처리
    PC_second_num = random.choice(answer_li)
    if PC_first_num == PC_second_num :
        continue
    break


# 정수로 전환 ( 열표와, 그냥표 구분필요 )
PC_first = int(PC_first_num)
PC_second = int(PC_second_num)


# 절대값으로 전환 ( 족보 전환을 위한 )
PC_first_abs = abs(PC_first)
PC_second_abs = abs(PC_second)

print(PC_first, PC_second)

# if PC_first in jockbo_goang_top and PC_second in jockbo_goang_top :
#     print("천하무적%s %s 광땡 떴다 족보!" % (PC_first, PC_second))
jockbo_goang_top_def(PC_first, PC_second)

if PC_first in jockbo_goang and PC_second in jockbo_goang :
    print("%s %s 광땡 떴다 족보!" % (PC_first, PC_second))

elif PC_first_abs == PC_second_abs:
    print("%s 땡 떴다 족보!" % PC_first_abs)

elif PC_first in jockbo_ali and PC_second in jockbo_ali :
    print("%s %s 알리 족보!" % (PC_first_abs, PC_second_abs))

elif PC_first in jockbo_docksa and PC_second in jockbo_docksa :
    print("%s %s 독사 족보!" % (PC_first_abs, PC_second_abs))

elif PC_first in jockbo_gubbing and PC_second in jockbo_gubbing :
    print("%s %s 구삥 족보!" % (PC_first_abs, PC_second_abs))

elif PC_first in jockbo_jangbbing and PC_second in jockbo_jangbbing :
    print("%s %s 장삥 족보!" % (PC_first_abs, PC_second_abs))

elif PC_first in jockbo_seluk and PC_second in jockbo_seluk :
    print("%s %s 세륙 족보!" % (PC_first_abs, PC_second_abs))


jockbo_kabo_def(PC_first_abs, PC_second_abs)












