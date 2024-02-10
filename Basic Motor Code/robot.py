import wpilib
from magicbot import MagicRobot
from components.motor import Motor
from components.hmi import HMI

class MyRobot(MagicRobot):
    motor1 : Motor
    motor2 : Motor


    def createObjects(self):
        
        self.HMI_controller = wpilib.XboxController(0)
        self.motor1 = Motor(0)
        self.motor2 = Motor(1)

    def disabledPeriodic(self):
        pass

    def teleopInit(self):
       pass

    def teleopPeriodic(self):
        if self.HMI_controller.getLeftTriggerAxis() != 0:
            self.motor1.spin(speed=self.HMI_controller.getLeftTriggerAxis())
        
        if self.HMI_controller.getRightTriggerAxis() != 0:
            self.motor2.spin(speed=self.HMI_controller.getRightTriggerAxis())
        
        
        pass


if __name__ == "__main__":
    wpilib.run(MyRobot)
