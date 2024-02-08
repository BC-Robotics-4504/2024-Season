import wpilib


class HMI:
    ''' HMI (Human Machine Interface) -- Xbox 360/One Controller
    REFERENCE: https://robotpy.readthedocs.io/projects/wpilib/en/latest/wpilib/XboxController.html#wpilib.XboxController
    '''
    xbox: wpilib.XboxController
    
    def __init__(self):
        # self.XboxController = wpilib.XboxController(controllerID)
        self.changed = True
        
        self.leftX = 0.
        self.leftY = 0.

        self.rightX = 0.
        self.rightY = 0.

    def updateAnalogSticks(self):
        # Get input from analog sticks 
        self.leftX = self.xbox.getLeftX()
        self.leftY = self.xbox.getLeftY()
        self.rightX = self.xbox.getRightX()
        self.rightY = self.xbox.getRightY()
        return False

    def getAnalogSticks(self):
        return self.leftX, self.leftY, self.rightX, self.rightY

    def execute(self):
        self.updateAnalogSticks()
