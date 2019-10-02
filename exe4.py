print ("\n\nExercise 4")


class AircraftNew(object):
    def __init__(self, x=0, y=0, acc=1):
        self.x = x
        self.y = y
        self._acc = acc

    def moveRight(self):
        self.x += 1

    def moveLeft(self):
        self.x += -1

    def moveUp(self):
        self.y += -1

    def moveDown(self):
        self.y += 1


aircraftNew = AircraftNew()
aircraftNew1 = AircraftNew(9, 9)
print ("AircraftNew X -", aircraftNew.x, ", Y -", aircraftNew.y)
print ("AircraftNew1 X -", aircraftNew1.x, ", Y -", aircraftNew1.y)
