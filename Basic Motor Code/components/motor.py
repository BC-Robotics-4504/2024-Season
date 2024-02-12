
import rev
import wpilib



class Motor:   
    def __init__(self, canID, motorType = rev.CANSparkMax.MotorType.kBrushless):
        self.canID = canID
        self.motorType = motorType
        self.motor = rev.CANSparkMax(self.canID, self.motorType)
        
        
        pass
    
    
    def spin(self, speed):
        self.motor.set(speed)
       

   