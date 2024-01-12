import wpilib
from magicbot import MagicRobot

class MyRobot(MagicRobot):

    def createObjects(self):
        pass

    def disabledPeriodic(self):
        pass

    def teleopInit(self):
        pass

    def teleopPeriodic(self):
        pass


if __name__ == "__main__":
    wpilib.run(MyRobot)
