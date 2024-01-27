import wpilib
from magicbot import MagicRobot
from motor import Motor


class MyRobot(MagicRobot):
    motor1: Motor
    motor2: Motor

    def createObjects(self):
        self.motor1 = Motor(canID=0)
        self.motor2 = Motor(canID=1)

        # Launcher Hardware Config

        # Climber Hardware Config

        # HMI Hardware Config
        self.HMI_controller = wpilib.XboxController(0)
        pass

    def disabledPeriodic(self):
        pass

    def teleopInit(self):
        # Define relationships between controller input events and what they're supposed to trigger
        # DO NOT PUT LEFT X/Y or RIGHT X/Y here--those will have to be updated using polling
        pass

    def teleopPeriodic(self):
        if self.HMI_controller.getAButtonPressed():
            self.motor1.isSpinning = True
            self.motor2.isSpinning = True
            self.motor1.spin()
            self.motor2.spin()

        if self.HMI_controller.getBButtonPressed():
            self.motor1.isSpinning = False
            self.motor2.isSpinning = False
            self.motor1.stop()
            self.motor2.stop()


if __name__ == "__main__":
    wpilib.run(MyRobot)
