import wpilib
from magicbot import MagicRobot
from SwerveDrive.swervemodule import SwerveModule

class MyRobot(MagicRobot):

    def createObjects(self):
        self.frontLeft_swerveModule = SwerveModule(1, 2)
        pass

    def disabledPeriodic(self):
        pass

    def teleopInit(self):
        pass

    def teleopPeriodic(self):
        pass


if __name__ == "__main__":
    wpilib.run(MyRobot)
