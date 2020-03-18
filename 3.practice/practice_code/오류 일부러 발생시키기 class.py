class MyError(Exception) :
    pass

def say_nick(nick) :
    if nick == "바보" :
        raise MyError()
    print(nick)

try :
    
    say_nick("천사")
    say_nick("바보")
except MyError :
    print("바보 하지마")

except MyError as e:    # MyError를 변수로 지정해서 출력도 가능함.
    print(e)
