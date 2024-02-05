import wpilib



class HMI:
    
    def __init__(self, ID):
        self.controller = wpilib.XboxController(ID)
        pass
    
    def getAnalog(self):
        return (self.controller.getX(), self.controller.getY())