# cal05.py

## 클래스 선언 부분 ##
class calc:
    def __init__(self, v1, v2, op):
        self.v1 = v1
        self.v2 = v2
        self.op = op
        self.result = 0
        
    def cal(self):
        if self.op == '+':
            result = self.v1 + self.v2
        elif self.op == '-':
            result = self.v1 - self.v2
        elif self.op == '*':
            result = self.v1 * self.v2
        elif self.op == '/':
            result = self.v1 / self.v2

        return result


