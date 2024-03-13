# import wpilib

import wpilib


class HMI:
    ''' HMI (Human Machine Interface) -- Xbox 360/One Controller
    REFERENCE: https://robotpy.readthedocs.io/projects/wpilib/en/latest/wpilib/XboxController.html#wpilib.XboxController
    '''
    xbox: wpilib.XboxController
    
    def __init__(self):
        self.changed = True
        
        # Analog Sticks

        self.leftX = 0.
        self.leftY = 0.
        self.rightX = 0.
        self.rightY = 0.
        
        # Buttons
        self.A = False
        self.B = False
        self.X = False
        self.Y = False

        # Bumpers
        self.RB = False
        self.LB = False

        # Triggers
        self.RT = 0.
        self.LT = 0.
   
        # Other
        self.start = False
        self.rightStickButton = False
        self.leftStickButton = False
    
        

    def updateAnalogSticks(self):
        # Get input from analog sticks 
        self.leftX = self.xbox.getLeftX()
        self.leftY = self.xbox.getLeftY()
        self.rightX = self.xbox.getRightX()
        self.rightY = self.xbox.getRightY()
        return False
    
    def updateButtons(self):
        self.A = self.xbox.getAButton()
        self.B = self.xbox.getBButton()
        self.X = self.xbox.getXButton()
        self.Y = self.xbox.getYButton()
        self.RT = self.xbox.getRightTriggerAxis()
        self.LT = self.xbox.getLeftTriggerAxis()
        self.RB = self.xbox.getRightBumper()
        self.LB = self.xbox.getLeftBumper()
        self.start = self.xbox.getStartButton()
        self.rightStickButton = self.xbox.getRightStickButtonPressed()
        self.leftStickButton = self.xbox.getLeftStickButtonPressed()
        return None
    
    def getA(self):
        A = self.A
        self.A = False
        return A
    
    def getX(self):
        X = self.X
        self.X = False
        return X
    
    def getY(self):
        Y = self.Y
        self.Y = False
        return Y
    
    def getB(self):
        B = self.B
        self.B = False
        return B
    
    def getRT(self):
        RT = self.RT
        self.RT = 0
        return RT
    
    def getLT(self):
        LT = self.LT
        self.LT = 0
        return LT
    
    def getRB(self):
        RB = self.RB
        self.RB = False
        return RB
    
    def getLB(self):
        LB = self.LB
        self.LB = False
        return  LB
    
    def getStart(self):
        START = self.start
        self.start = False
        return START
    
    def getRightStickButton(self):
        RSB = self.rightStickButton
        self.rightStickButton = False
        return RSB
    
    def getLeftStickButton(self):
        LSB = self.leftStickButton
        self.leftStickButton = False
        return LSB

    def getAnalogSticks(self):
        return self.leftX, self.leftY, self.rightX, self.rightY

    def execute(self):
        self.updateAnalogSticks()
        self.updateButtons()
    