from subsystems import climber_system, drivetrain_system, launcher_system

import wpilib

from magicbot import MagicRobot
from networktables import NetworkTables


class MyRobot(MagicRobot):
    # Create low-level object
    drivetrain: drivetrain_subsystem
    launcher: launcher_subsystem
    climber: climber_subsystem

    def createObjects(self):
        return None

    def disabledPeriodic(self):
        return None

    def teleopInit(self):
        return None

    def teleopPeriodic(self):
        return None


if __name__ == "__main__":
    wpilib.run(MyRobot)
