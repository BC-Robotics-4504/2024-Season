import rev
import wpilib


class SparkMax():
    def __init__(self, canID, mtype):
        self.mtype = mtype
        self.canID = canID
        self.motor = rev.CANSparkMax(self.canID, self.mtype)
        self.isSpinning = False
    

    def spin(self):
        if self.isSpinning == True:
            self.motor.set(speed=.50)
        else:
            self.isSpinning == False