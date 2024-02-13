from re import X
import wpilib
from magicbot import MagicRobot
from components.motor import Motor
from components.hmi import HMIModule, XboxHMI

class MyRobot(MagicRobot):
    motor1 : Motor
    motor2 : Motor
    hmi: HMIModule


    def createObjects(self):

        self.motor1 = Motor(0)
        self.motor2 = Motor(1)
        self.hmi_interface = XboxHMI(0)

    def disabledPeriodic(self):
        pass

    def teleopInit(self):
       pass

    def teleopPeriodic(self):
        if self.hmi.getButton("A"):
            self.motor1.spin(.25)
        
        if self.hmi.getButton("B"):
            self.motor2.spin(.25)



if __name__ == "__main__":
    wpilib.run(MyRobot)
