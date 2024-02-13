import wpilib
from magicbot import MagicRobot
import math
import rev
import math

from components.swerveDrive.swerveDrive import SwerveDrive, SparkMaxTurning, SparkMaxDriving
from components.config import RobotConfig
from components.hmi.hmi import HMI
from components.launcher.launcher import Launcher, LauncherController

class MyRobot(MagicRobot):
    ''' MagicRobot Framework
    REFERENCE: https://robotpy.readthedocs.io/en/stable/frameworks/magicbot.html
    '''
    
    # # Swerve Drive Component Code
    DriveConfig: DriveConfig = RobotConfig(1.0, 1.0, speed_clamp=0.25)
    SwerveDrive: SwerveDrive
    
    # Controller Component Code
    HMI: HMI

    # Launcher Component Code
    Launcher: Launcher

    # Climber Component Code    

    def createObjects(self):
        # Swerve Drive Hardware Config
        self.SwerveDrive_FrontLeftAngleMotor = SparkMaxTurning(6, inverted=False, gear_ratio=1, wheel_diameter=1,
                                                          absolute_encoder=True, z_offset=0)
        self.SwerveDrive_FrontLeftSpeedMotor = SparkMaxDriving(5, inverted=False, gear_ratio=1, wheel_diameter=1)

        self.SwerveDrive_RearLeftAngleMotor = SparkMaxTurning(8, inverted=False, gear_ratio=1, wheel_diameter=1,
                                                          absolute_encoder=True, z_offset=0)
        self.SwerveDrive_RearLeftSpeedMotor = SparkMaxDriving(7, inverted=False, gear_ratio=1, wheel_diameter=1)

        self.SwerveDrive_RearRightAngleMotor = SparkMaxTurning(2, inverted=False, gear_ratio=1, wheel_diameter=1,
                                                          absolute_encoder=True, z_offset=0)
        self.SwerveDrive_RearRightSpeedMotor = SparkMaxDriving(1, inverted=False, gear_ratio=1, wheel_diameter=1)

        self.SwerveDrive_FrontRightAngleMotor = SparkMaxTurning(4, inverted=False, gear_ratio=1, wheel_diameter=1,
                                                          absolute_encoder=True, z_offset=0)
        self.SwerveDrive_FrontRightSpeedMotor = SparkMaxDriving(3, inverted=False, gear_ratio=1, wheel_diameter=1)
        

        # Launcher Hardware Config

        # Climber Hardware Config

        # HMI Hardware Config
        self.HMI_xbox = wpilib.XboxController(0)
        pass

    def disabledPeriodic(self):
        pass

    def teleopInit(self):
        # Define relationships between controller input events and what they're supposed to trigger
        # DO NOT PUT LEFT X/Y or RIGHT X/Y here--those will have to be updated using polling
        # self.SwerveDrive.clearFaults()
        pass

    def teleopPeriodic(self):
        # 1.) Poll position of Left X/Y and Right X/Y from controller
        Lx, Ly, Rx, _ = self.HMI.getAnalogSticks()

        # 2.) Move drivetrain based on Left X/Y and Right X/Y controller inputs
        self.SwerveDrive.move(Lx, Ly, Rx)


if __name__ == "__main__":
    wpilib.run(MyRobot)
