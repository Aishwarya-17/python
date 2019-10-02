print ("\n\nExercise 2")


class Aircraft(object):
    def __init__(self):
        self.x = 0
        self.y = 0
        self.acc = 1

    def moveRight(self):
        self.x += 1

    def moveLeft(self):
        self.x += -1

    def moveUp(self):
        self.y += -1

    def moveDown(self):
        self.y += 1


aircraft = Aircraft()
aircraft.moveDown()
aircraft.moveDown()
aircraft.moveUp()
aircraft.moveLeft()
aircraft.moveLeft()
aircraft.moveRight()
aircraft.moveDown()
aircraft.moveDown()
aircraft.moveUp()
aircraft.moveLeft()
aircraft.moveLeft()
aircraft.moveRight()
print ("Aircraft X -", aircraft.x, ", Y -", aircraft.y)
