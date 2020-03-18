PI = 3.141592

class Math :
    def solv(self,r) :
        return PI * (r**2)

def add(a,b) :
    return a + b

if __name__ == "__main__":
    print(PI)
    a = Math()
    print(a.solv(20))
    print(add(PI, 4.4))
