import rev
import wpilib


class Motor:
    def __init__(self, canID, mtype):
        self.canID = canID
        self.mtype = mtype
        self.motor = rev.CANSparkMax(mtype="brushless")
        self.isSpinning = False

    def spin(self):
        self.isSpinning = True
        if self.isSpinning == True:
            rev.CANSparkMax.set(speed=0.25)
        else:
            rev.CANSparkMax.set(speed=0)

    def stop(self):
        rev.CANSparkMax.set(speed=0)
