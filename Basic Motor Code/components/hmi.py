import wpilib



class HMI:
    
    def __init__(self, ID):
        self.controller = wpilib.XboxController(ID)
        pass
    
    def getAnalog(self):
        return (self.controller.getLeftY(), self.controller.getRightY())

    def getLeftTrigger(self):
        return float(self.controller.getLeftTriggerAxis())

    def getRightTrigger(self):
        return float(self.controller.getRightTriggerAxis())

    