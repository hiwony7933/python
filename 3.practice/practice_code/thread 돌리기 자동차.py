import time
import threading 

class RacingCar :
    def __init__(self, name) :
        self.carName = name

    def runCar(self) :
        for i in range(0, 5) :
            carStr = self.carName + '~%d 번 달림니다. \n' % (i+1)
            print(carStr, end="")
            time.sleep(0.1)

car1 = RacingCar("H자동차")
car2 = RacingCar("K자동차")
car3 = RacingCar("O자동차")

th1 = threading.Thread(target = car1.runCar)
th2 = threading.Thread(target = car2.runCar)
th3 = threading.Thread(target = car3.runCar)

th1.start()
th2.start()
th3.start()

th1.join()
th2.join()
th3.join()
