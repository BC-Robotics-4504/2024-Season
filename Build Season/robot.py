import wpilib
from magicbot import MagicRobot
from components.swerveDrive.swervemodule import SwerveModule

class MyRobot(MagicRobot):

    def createObjects(self):
        self.frontLeft_swerveModule = SwerveModule(6, 5)
        self.frontRight_swerveModule = SwerveModule(4, 3)
        self.rearRight_swerveModule = SwerveModule(2, 1)
        self.rearLeft_swerveModule = SwerveModule(8, 7)
        pass

    def disabledPeriodic(self):
        pass

    def teleopInit(self):
        self.frontLeft_swerveModule.move(0.1, 3)
        self.frontRight_swerveModule.move(0.1, 3)
        self.rearLeft_swerveModule.move(0.1, 3)
        self.rearRight_swerveModule.move(0.1, 3)
        pass

    def teleopPeriodic(self):
        pass


if __name__ == "__main__":
    wpilib.run(MyRobot)
