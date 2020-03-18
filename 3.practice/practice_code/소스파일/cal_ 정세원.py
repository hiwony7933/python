# -*- coding: utf-8 -*-
"""
Created on Fri Dec 13 14:32:23 2019

@author: sjeong
"""

def cal(oper,a,b):
    
    if oper=="+":
        return a+b
    elif oper=="-":
        return a-b
    elif oper=="*":
        return a*b
    elif oper=="/":
        return a/b
    
while True:    
    oper=str(input("계산 구분을 입력하세요(+,-,*,/):"))
    cal_list=("+", "-","*")
    a=int(input("첫번째 수를 입력하세요:"))
    b=int(input("두번째 수를 입력하세요:"))
    if oper in cal_list:
        print("계산기:%d%s%d = %d입니다"%(a,oper,b,cal(oper,a,b)))
    elif oper=="/":
        if b!=0:
            print("계산기:%d%s%d = %d입니다"%(a,oper,b,cal(oper,a,b)))
        else:
            print("0으로 나눌 수 없습니다.")
            break        
    else:
        break

