print ("\n\nExercise 6")


class AircraftNew2(object):
    def __init__(self, xOrg=0, yOrg=0, xDes=0, yDes=0, acc=1):
        self.xOrg = xOrg
        self.yOrg = yOrg
        self.xDes = xDes
        self.yDes = yDes
        self.slope = 0
        self.path = []
        self.b = 0
        self.calculateSlope()
        self.calculateB()
        self.calculatePath()

    def calculateSlope(self):
        self.slope = ((self.yOrg - self.yDes) / (self.xOrg - self.xDes))

    def calculateB(self):
        self.b = self.yOrg - (self.slope * self.xOrg)

    def calculatePath(self):
        path = []
        for x in range(self.xOrg + 1, self.xDes + 1):
            y = (self.slope * x) + self.b
            path.append((x, y))
        self.path = path

    def printValues(self):
        print ("Starting Point(", self.xOrg, ",", self.yOrg, ")")
        print ("Ending Point(", self.xDes, ",", self.yDes, ")")
        print ("Slope", self.slope)
        print ("b", self.b)
        print ("Equation(y= mx +b ) - y =", self.slope, "x +", self.b)

    def printPath(self):
        for i in self.path:
            print ("Accelerating-", i)
        print ("We have arrived")


a = AircraftNew2(12, 10, 17, 80)
a.printValues()
a.printPath()
