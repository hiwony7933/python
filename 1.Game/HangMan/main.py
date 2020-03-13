# 답안 txt 의 추출 (파싱이용)

import random
import pyautogui as pag
import time

# 답안 파일 list 저장
answer_li = []     # 답안 깡통 list 만들고

# txt 파일의 답안은 엔터방식
f = open("./answer.txt", "r")
answer_li = f.readlines()
f.close()

for i in range(len(answer_li)):
    answer_li[i] = answer_li[i].strip().replace(
        " ", "")   # 맨마지막 list 에 공란이 들어가서 지움

push = ""

while push != "stop":
    answer_Text = ""  # 정답 초기화
    pag.countdown(3)
    if not answer_li:
        print("정답이 모두 소진되었습니다.")
        break
    else:
        answer_Text = random.choice(answer_li)  # 정답 list 에서 랜덤으로 객체 불러오기
        answer_li.remove(answer_Text)

        Text_li = list(answer_Text)        # 정답 단어의 list 처리
        Text_len = len(answer_Text)     # 정답 단어의 총 글자 수
        Text_IP_list = list("-" * Text_len)     # 정답 단어의 총 글수 만큼 하이픈 처리

        Text_use_IP_text = ""   # 답안제출 변수, 없어도 되는데 어떤 변수인지 보기 쉽게 하기 위해서
        Empty_Text_li = []     # 유저가 입력하는 답안의 저장 list 화 (중복제외)

        while True:  # 목숨에 대한 입력 에러 처리 반복문
            Life_IP_Text = input("\n몇개의 목숨으로 도전하시겠습니까? : ")

            if Life_IP_Text.isalpha() or Life_IP_Text == "":
                print("\nwarnings : 다시 숫자로 입력하세요.")
                continue  # 입력하는 글자가 숫자가 아니면 반복, 숫자면 다음 수행

            elif Life_IP_Text.isdigit() != True:   # 문자 숫자 믹스 입력 방지
                print("\nwarnings : 다시 숫자로 입력하세요.")
                continue  # 입력하는 글자가 숫자가 아니면 반복, 숫자면 다음 수행

            elif abs(int(Life_IP_Text)) > 10:      # 음수 또는 소수 입력 방지
                print("\nwarnings : 1 ~ 10까지 입력하세요.")
                continue  # 입력하는 숫자의 자리수가 2개 이하가 아니면 반복

            break
        Life_IP_int = int(Life_IP_Text)

        print("[", "-" * Text_len, "]", "*숨겨진 단어는 총 %s 글자 입니다.*" % Text_len)    # Text_IP_text 의 총 글자 수만큼 " - " 출력

        while Life_IP_int != 0:   # 목숨이 0개가 되면 while 문 탈출
            print("\n목숨이 %d 개 있습니다." % Life_IP_int)

            if Text_IP_list != Text_li:         # 입력되는 답안 list 와 정답 list 가 틀리면 지속 수행

                while True:        # use input 에 대한 반복문
                    Text_use_IP_text = input("\n글자 입력하세요 : ")

                    if Text_use_IP_text.isalpha() != True:
                        print("\nwarnings : 다시 문자로 입력하세요.")
                        continue   # 입력하는 글자가 문자가 아니면 반복, 문자면 다음 수행

                    elif len(Text_use_IP_text) != 1:
                        print("\nwarnings : 한글자만 입력하세요.")
                        continue    # 입력하는 글자의 수가 1개가 아니면 반복

                    # Empty_list(없는 list)에 입력된 글자를 찾으면 True
                    elif Text_use_IP_text in Empty_Text_li:
                        print("\n이미 입력하셨습니다.")
                        continue

                    break

                # 제출된 답안의 중복을 피하기 위한 Empty_list 에 추가함.
                Empty_Text_li.append(Text_use_IP_text)

                Flag = False        # 정답, 오답을 걸러내는 Flag 선언
                for i in range(Text_len):  # 정답 list 에서 정답 글자 수 만큼 순차적으로 비ㄴ세교함.

                    if Text_li[i] == Text_use_IP_text:  # 정답 list 순번대로 입력된 답안 글자와 맞는지 반복 수행
                        # 정답 list 안에 제출된 글자가 있으면 그 위치의 하이픈을 글자로 변경
                        Text_IP_list[i] = Text_use_IP_text
                        print("맞습니다.\n\n", Text_IP_list)
                        Flag = True

                if Flag == False:  # 정답일경우 Flag=True 임으로 거짓 continue , 오답일경우 Flag=False, if 문 수행
                    Life_IP_int = Life_IP_int - 1
                    print("\n입력하신 답안은",Empty_Text_li)
                    print("\n오답입니다. 목숨이 1개 줄었습니다.")
                    if Life_IP_int == 0:
                        print("\n입력하신 답안은",Empty_Text_li)
                        print("\n목숨을 모두 소진했습니다.")
                        time.sleep(2)
                        # print("\n정답은 %s 입니다. " % answer_Text)

                continue

            else:
                print("\n정답입니다. 수고하셨습니다.")
            break

    print("-" * 50)
    time.sleep(2)
    push = input("\n계속할꺼면 엔터 혹은 아무키나 입력 후 엔터, 안할꺼면 stop 입력 : ")


# 파일 입출력 (완료)
# 파일 list 저장 , list 불러오고 (완료)
# 정답목숨을 토탈목숨에서 안깍기게 수정 ( 완료 )
# txt에서 불러온 list 에서 랜덤으로 문제 출력 (완료)

# 두번째 문제 출력 할때 중복안되게.(완료)
# 다음문제 진행할때 엔터 (완료)
