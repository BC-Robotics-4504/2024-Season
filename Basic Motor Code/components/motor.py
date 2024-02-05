
import rev



class Motor:   
    def __init__(self, canID, motorType = rev.CANSparkMax.MotorType.kBrushless):
        self.canID = canID
        self.motorType = motorType
        self.motor = rev.CANSparkMax(self.canID, self.motorType)
        self.isSpinning = False
        pass
    
    
    def spin(self, speed):
        if self.isSpinning:
            self.motor.set(speed)
        else:
            self.motor.set(0)

   