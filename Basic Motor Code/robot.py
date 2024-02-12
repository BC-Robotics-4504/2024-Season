import wpilib
from magicbot import MagicRobot
from components.motor import Motor
from components.hmi import HMI

class MyRobot(MagicRobot):
    motor1 : Motor
    motor2 : Motor
    HMI_controller : HMI


    def createObjects(self):

        self.motor1 = Motor(0)
        self.motor2 = Motor(1)
        self.HMI_controller = HMI(0)

    def disabledPeriodic(self):
        pass

    def teleopInit(self):
       pass

    def teleopPeriodic(self):
        
        self.motor1.spin(self.HMI_controller.getLeftTrigger())
        self.motor2.spin(self.HMI_controller.getRightTrigger())
        
        
        pass


if __name__ == "__main__":
    wpilib.run(MyRobot)
