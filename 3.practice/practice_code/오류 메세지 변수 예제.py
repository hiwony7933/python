try :
    a = [1, 2]
    print(a[4])
    4/0

except IndexError as e:
    print(e)

except ZeroDivisionError as e:
    # 인터크립터 언어 특성상 순서대로 처리하기때문에 print문의 에러 수행
    print(e)
    

#except (IndexError, ZeroDivisionError) as e:  #2개 이상 오류 동시처리 가능
    #print(e)
