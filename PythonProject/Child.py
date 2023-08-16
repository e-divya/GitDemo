from FirstDemo import Calculator


class childCalc(Calculator):
    num2 = 200

    def __init__(self):
        Calculator.__init__(self, 10, 20)
    def getCompleteData(self):
        return self.num2 + self.num + self.Summation()

obj = childCalc()
print(obj.getCompleteData())
