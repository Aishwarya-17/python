print ("\n\nExercise 5")

import numpy


class AircraftNew1(object):
    def __init__(self, xOrg=0, yOrg=0, xDes=0, yDes=0, acc=1):
        self.xOrg = xOrg
        self.yOrg = yOrg
        self.xDes = xDes
        self.yDes = yDes

    def printValues(self):
        print ("Starting Point(", self.xOrg, ",", self.yOrg, ")")
        print ("Ending Point(", self.xDes, ",", self.yDes, ")")


Boeing_747 = AircraftNew1(numpy.random.randint(2, 100), numpy.random.randint(2, 100), numpy.random.randint(2, 100),
                          numpy.random.randint(2, 100))
Boeing_747.printValues()

