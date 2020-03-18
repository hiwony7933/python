# -*- coding: utf-8 -*-
"""
Created on Thu Dec 12 14:11:05 2019

@author: admin
"""

def coffee_machine(num, nick):
        num=int(num)
        nick=str(nick)
        print("#1. 뜨거운 물을 준비한다.")
        print("#2. 종이컵을 준비한다")
        if num==1:
            print("#3. 아메리카노를 탄다")
        elif num==2:
            print("#3. 카페라떼를 탄다.")
        elif num==3:
            print("#3. 카푸치노를 탄다.")
        else:
            print("#3. 아무거나 탄다.")
        print("#4. 물을 붓는다.")
        print("#5. 스푼으로 젓는다")
        print("%s님 커피 여기 있습니다"%nick)
        

coffee=int(input("어떤 커피 드릴까요(1:아메리카노, 2:카페라떼, 3:카푸치노):"))
nick=str(input("닉네임을 입력해주세요:"))

while True:
    if coffee in range(1,4):
        coffee_machine(coffee,nick)
        coffee=int(input("어떤 커피 드릴까요(1:아메리카노, 2:카페라떼, 3:카푸치노):"))
        nick=str(input("닉네임을 입력해주세요:"))
    else:
        break