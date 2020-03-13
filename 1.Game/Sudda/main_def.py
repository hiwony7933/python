
import random

jockbo_goang_top = [3, 8]   # 삼팔광땡 족보
jockbo_goang = [1, 8]    # 광땡 족보
jockbo_ddang = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]   # 땡 족보 안씀
jockbo_ali = [1, 2]
jockbo_docksa = [1, 4]
jockbo_gubbing = [1, 9]
jockbo_jangbbing = [1, 10]
jockbo_seluk = [4, 6]

def jockbo_goang_top_def(first, second):
    if first in jockbo_goang_top and second in jockbo_goang_top :
        print("천하무적%s %s 광땡 떴다 족보!" % (PC_first_abs, PC_second_abs))
    return

def jockbo_goang_def(first, second):
    if first in jockbo_goang and second in jockbo_goang:
        print("%s %s 광땡 떴다 족보!" % (PC_first, PC_second))
    return

def jockbo_ddang_def(first, second):
    if first == second:
        print("%s 땡 떴다 족보!" % PC_first_abs)
    return

def jockbo_ali_def(first, second):
    if first in jockbo_ali and second in jockbo_ali:
        print("%s %s 알리 족보!" % (PC_first_abs, PC_second_abs))
    return

def jockbo_doksa_def(first, second):
    if first in jockbo_docksa and second in jockbo_docksa:
        print("%s %s 독사 족보!" % (PC_first_abs, PC_second_abs))
    return

def jockbo_gubbind_def(first, second):
    if first in jockbo_gubbing and second in jockbo_gubbing :
        print("%s %s 구삥 족보!" % (PC_first_abs, PC_second_abs))
    return

def jockbo_jangbbind_def(first, second) :
    if first in jockbo_jangbbing and second in jockbo_jangbbing :
        print("%s %s 장삥 족보!" % (PC_first_abs, PC_second_abs))
    return

def jockbo_seluk_def(first, second):
    if first in jockbo_seluk and second in jockbo_seluk :
        print("%s %s 세륙 족보!" % (PC_first_abs, PC_second_abs))
    return

def jockbo_kabo_def(first, second):
    if (first + second) == 9:
        print("%s %s 갑오 족보!" % (PC_first_abs, PC_second_abs))
    elif (first + second) == 19:
        print("%s %s 갑오 족보!" % (PC_first_abs, PC_second_abs))
    return

def jockbo_kkt_def(first, second):
    if (first + second) in range(1, 9):
        print("%s 끗" % (PC_first_abs + PC_second_abs))
    elif ((first + second) % 10) in range(1, 9):
        print("%s 끗" % ((PC_first_abs + PC_second_abs) % 10))
    return

def jockbo_mang_def(first, second):
    if (first + second) == 10:
        print("%s 망통" % (PC_first_abs + PC_second_abs))
    return

# 양수는 열자리, 광
answer_li = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, -1, -2, -3, -4, -5, -6, -7, -8, -9, -10]

while True :
    insert_coin = input("동전을 입력하세요 ")
    if insert_coin.isdigit() != True:
        print("다시 입력하세요")
        continue

    elif len(insert_coin) >= 10:
        print("최대 동전은 10개까지 넣을수있습니다.")
        continue
    break

push = ""
while push != "stop":
    PC_first = random.choice(answer_li)

    while True:    # first 카드와 second 카드의 중복 제외 처리
        PC_second = random.choice(answer_li)
        if PC_first == PC_second:
            continue
        break

    # 절대값으로 전환 ( 족보 전환을 위한 )
    PC_first_abs = abs(PC_first)
    PC_second_abs = abs(PC_second)

    print(PC_first, PC_second)
    print("PC (- -)")

    # PC 출력 족보


    jockbo_goang_top_def(PC_first, PC_second)
    jockbo_goang_def(PC_first, PC_second)
    jockbo_ddang_def(PC_first_abs, PC_second_abs)
    jockbo_ali_def(PC_first_abs, PC_second_abs)
    jockbo_doksa_def(PC_first_abs, PC_second_abs)
    jockbo_gubbind_def(PC_first_abs, PC_second_abs)
    jockbo_jangbbind_def(PC_first_abs, PC_second_abs)
    jockbo_seluk_def(PC_first_abs, PC_second_abs)
    jockbo_kabo_def(PC_first_abs, PC_second_abs)
    jockbo_kkt_def(PC_first_abs, PC_second_abs)
    jockbo_mang_def(PC_first_abs, PC_second_abs)

    insert_coin = int(insert_coin) - 1
    print("%d 판 남았습니다." % insert_coin)
    push = input("계속 하시겠습니까? 그만하려면 stop 입력 : ")
    continue









