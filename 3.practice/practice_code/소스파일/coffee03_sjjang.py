# coffee_machine

def coffee_machine(button):

     print ("#1 뜨거운 물을 준비한다")
     print ("#2 종이컵을 준비한다")
     if button == 1:
          print("#3 아메리카노를 탄다.")
     elif button == 2:
          print("#3 카페라떼를 탄다.")

     else:
          print("#3 카푸치노를 탄다.")
     print ("#4 물을 붓는다")
     print ("#5 스푼으로 젓는다.")

cup = 100

while cup:
     print ("현재 %d잔 주문 가능합니다" %cup)
     button = int(input("어떤 커피를 드릴까요? (1번 아메리카노// 2번 카페라떼 // 3번 카푸치노 // 4번 나가기) : "))

     if button <= 3:
          nick = input("닉네임을 알려주세요: ")
          coffee_machine(button)
          print ("=" * 50)
          print("%s님이 주문하신 메뉴 나왔습니다" %nick)
          cup -= 1
          print("앞으로 %d잔 주문 가능합니다" %cup)
          print ("=" * 50)

     elif button ==4:
          print("주문을 종료합니다")
          break

     else:
          print("잘못 누르셨습니다")
          continue
