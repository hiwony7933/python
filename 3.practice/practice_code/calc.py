class calc :
    def __init__(self, a, b, c) :
        self.a = a
        self.b = b
        self.c = c
    def cal(self) :
        if self.c == "+" :
            result = self.a + self.b
        elif self.c == "-" :
            result = self.a - self.b
        elif self.c == "*" :
            result = self.a * self.b
        elif self.c == "/" :
            result = self.a / self.b
        return result
