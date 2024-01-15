import wpilib
from magicbot import MagicRobot

from components.swerveDrive.swervemodule import SwerveModule
from components.hmi.hmi import HMI

class MyRobot(MagicRobot):

    def createObjects(self):
        self.frontLeft_swerveModule = SwerveModule(angle_canID=6, speed_canID=5)
        self.frontRight_swerveModule = SwerveModule(angle_canID=4, speed_canID=3)
        self.rearRight_swerveModule = SwerveModule(angle_canID=2, speed_canID=1)
        self.rearLeft_swerveModule = SwerveModule(angle_canID=8, speed_canID=7)
        self.HMI = HMI(controllerID=0)
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
        # 1.) Check HMI has been updated (new inputs detected)
        # 2.) If something has happened, do the thing


if __name__ == "__main__":
    wpilib.run(MyRobot)
