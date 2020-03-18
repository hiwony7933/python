class Bird :
    def fly(self) :
        raise NotImplementedError


class Eagle(Bird) :
    pass
try :
    eagle = Egale()     # 철자 틀림 
    eagle.fly()
except NameError as e:    # as e: 변수로 정의 
    print(e)



