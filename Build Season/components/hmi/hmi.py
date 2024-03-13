# import wpilib

import wpilib


class HMI:
    ''' HMI (Human Machine Interface) -- Xbox 360/One Controller
    REFERENCE: https://robotpy.readthedocs.io/projects/wpilib/en/latest/wpilib/XboxController.html#wpilib.XboxController
    '''
    xbox: wpilib.XboxController
    
    def __init__(self):
        
        """ HMI.__init__() -> None
        
        Initialize the HMI object."""
        
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
        
        #Dpad
        self.DpadUp = False
        self.DpadDown = False
   
        # Other
        self.start = False
        self.rightStickButton = False
        self.leftStickButton = False
        

    def updateAnalogSticks(self):
        """HMI.updateAnalogSticks() -> False
        
        Update the analog sticks on the controller."""
        # Get input from analog sticks 
        self.leftX = self.xbox.getLeftX()
        self.leftY = self.xbox.getLeftY()
        self.rightX = self.xbox.getRightX()
        self.rightY = self.xbox.getRightY()
        return False
        
    def updateButtons(self):
        """HMI.updateButtons() -> None
        
        Update the buttons on the controller."""
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
        rawDpad = self.xbox.getPOV()
        
        if rawDpad != -1:
            if rawDpad == 0 or rawDpad == 315 or rawDpad == 45: #Dpad up
                self.DpadUp = True
                
            if rawDpad == 135 or rawDpad == 180 or rawDpad == 225: #Dpad down
                self.DpadDown = True

        return None
    
    def getA(self):
        """HMI.getA() -> bool
        
        return the state of the A button."""
        A = self.A
        self.A = False
        return A
    
    def getX(self):
        """HMI.getX() -> bool
        
        return the state of the X button."""
        X = self.X
        self.X = False
        return X
    
    def getY(self):
        """HMI.getY() -> bool
        
        return the state of the Y button."""
        Y = self.Y
        self.Y = False
        return Y
    
    def getB(self):
        """HMI.getB() -> bool
        
        return the state of the B button."""
        B = self.B
        self.B = False
        return B
    
    def getRT(self):
        """" HMI.getRT() -> float
        
        return the value of the right trigger."""
        RT = self.RT
        self.RT = 0
        return RT
    
    def getLT(self):
        """getLT() -> float
        
        return the value of the left trigger.
        """
        LT = self.LT
        self.LT = 0
        return LT
    
    def getRB(self):
        """HMI.getRB() -> bool
        
        return the state of the right bumper."""
        RB = self.RB
        self.RB = False
        return RB
    
    def getLB(self):
        """HMI.getLB() -> bool
        
        return the state of the left bumper."""
        LB = self.LB
        self.LB = False
        return  LB
    
    def getStart(self):
        """HMI.getStart() -> bool
        
        return the state of the start button."""
        START = self.start
        self.start = False
        return START
    
    def getRightStickButton(self):
        """HMI.getRightStickButton() -> bool
        
        return the state of the right stick button. """
        
        RSB = self.rightStickButton
        self.rightStickButton = False
        return RSB
    
    def getLeftStickButton(self):
        """HMIgetLeftStickButton() -> bool
        
        return the state of the left stick button."""
        LSB = self.leftStickButton
        self.leftStickButton = False
        return LSB

    def getAnalogSticks(self):
        """HMI.getAnalogSticks() -> (float, float, float, float)
        
        return the state of the analog sticks."""
        return self.leftX, self.leftY, self.rightX, self.rightY
    
    def getDpadUp(self):
        DPAD_UP = self.DpadUp
        self.DpadUp = False
        return DPAD_UP
    
    def getDpadDown(self):
        DPAD_DOWN = self.DpadDown
        self.DpadDown = False
        return DPAD_DOWN

    def execute(self):
        self.updateAnalogSticks()
        self.updateButtons()
    