import wpilib


class HMI:
    ''' HMI (Human Machine Interface) -- Xbox 360/One Controller
    REFERENCE: https://robotpy.readthedocs.io/projects/wpilib/en/latest/wpilib/XboxController.html#wpilib.XboxController
    '''
    controller: wpilib.XboxController
    
    def __init__(self, controllerID=0):
        # self.XboxController = wpilib.XboxController(controllerID)
        self.changed = True
        
        self.leftX = 0.
        self.leftY = 0.

        self.rightX = 0.
        self.rightY = 0.

    def updateAnalogSticks(self):
        # Get input from analog sticks 
        self.leftX = self.controller.getLeftX()
        self.leftY = self.controller.getLeftY()
        self.rightX = self.controller.getRightX()
        self.rightY = self.controller.getRightY()
        return False

    def getAnalogSticks(self):
        return self.leftX, self.leftY, self.rightX, self.rightY

    def execute(self):
        self.updateAnalogSticks()
