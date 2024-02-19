import wpilib
from magicbot import MagicRobot
import math
import rev
import math

from components.swerveDrive.swerveDrive import SwerveDrive, SparkMaxTurning, SparkMaxDriving
from components.config import RobotConfig
from components.hmi.hmi import HMI
from components.launcher.launcher import Launcher, SparkMaxDualSpinner, SparkMaxPivot
from components.climber.climber import Climber, SparkMaxClimb

from components.launcher.launcherController import LauncherController
from components.climber.climberController import ClimberController


class MyRobot(MagicRobot):
    ''' MagicRobot Framework
    REFERENCE: https://robotpy.readthedocs.io/en/stable/frameworks/magicbot.html
    '''
    
    RobotConfig = RobotConfig()
    
    # Swerve Drive Component Code
    SwerveDrive: SwerveDrive
    
    # Controller Component Code
    HMI: HMI

    # Launcher Component Code
    Launcher: Launcher
    LauncherController: LauncherController

    # Climber Component Code    
    Climber: Climber
    ClimberController: ClimberController

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
        self.Launcher_LauncherSpinnerL = SparkMaxDualSpinner(9, inverted=True)
        self.Launcher_LauncherSpinnerR = SparkMaxDualSpinner(10)

        self.Launcher_IntakeSpinnerL = SparkMaxDualSpinner(11, inverted=True)
        self.Launcher_IntakeSpinnerR = SparkMaxDualSpinner(12, inverted=True)

        # self.Launcher_IntakePivot = SparkMaxPivot(?) #FIXME!!!
        
        # Climber Hardware Config
        # self.Climber_ClimberMotorL = SparkMaxClimb(?) #FIXME!!!
        # self.Climber_ClimberMotorR = SparkMaxClimb(?, inverted=True) #FIXME!!!

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

        # 1.) Move drivetrain based on Left X/Y and Right X/Y controller inputs
        Lx, Ly, Rx, _ = self.HMI.getAnalogSticks()

        self.SwerveDrive.move(Lx, Ly, Rx)

        # 2.) Actuate Launcher
        if self.HMI.getA():
            self.LauncherController.lowerIntake()

        elif self.HMI.getB():
            self.LauncherController.raiseIntake()

        elif self.HMI.getLT() > 0.35:
            self.LauncherController.shootLauncher()

        self.LauncherController.run()

        #3.) Actuate Climber
        if self.HMI.getRB():
            self.ClimberController.raiseClimber()

        elif self.HMI.getLB():
            self.ClimberController.lowerClimber()

        self.ClimberController.run()

if __name__ == "__main__":
    wpilib.run(MyRobot)
