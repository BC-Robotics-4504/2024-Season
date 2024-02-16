import wpilib
from magicbot import MagicRobot
import math
import rev
import math

from components.swerveDrive.swerveDrive import SwerveDrive, SparkMaxTurning, SparkMaxDriving
from components.config import RobotConfig
from components.hmi.hmi import HMI
from components.launcher.launcher import Launcher, SparkMaxDualSpinner, SparkMaxPivot


class MyRobot(MagicRobot):
    ''' MagicRobot Framework
    REFERENCE: https://robotpy.readthedocs.io/en/stable/frameworks/magicbot.html
    '''
    
    RobotConfig = RobotConfig()
    
    # Swerve Drive Component Code
    SwerveDrive: SwerveDrive
    # SwerveDrive_FrontLeftAngleMotor: SparkMaxTurning
    # SwerveDrive_FrontLeftSpeedMotor: SparkMaxDriving
    
    # SwerveDrive_FrontRightAngleMotor: SparkMaxTurning
    # SwerveDrive_FrontRightSpeedMotor: SparkMaxDriving
    
    # SwerveDrive_RearLeftAngleMotor: SparkMaxTurning
    # SwerveDrive_RearLeftSpeedMotor: SparkMaxDriving
    
    # SwerveDrive_RearRightAngleMotor: SparkMaxTurning
    # SwerveDrive_RearRightSpeedMotor: SparkMaxDriving
    
    # Controller Component Code
    HMI: HMI

    # Launcher Component Code
    # Launcher: Launcher

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
        self.leftFly = SparkMaxDualSpinner(9, inverted=True)
        self.rightFly = SparkMaxDualSpinner(10)
        
        self.leftIntake = SparkMaxDualSpinner(11, inverted= True)
        self.rightIntake= SparkMaxDualSpinner(12, inverted=True)
        
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
        
        
        if self.HMI.getA():
            self.leftFly.setSpeed(.88)
            self.rightFly.setSpeed(.88)
        else:
            self.leftFly.setSpeed(0)
            self.rightFly.setSpeed(0)  
                        
        # if self.HMI.getB():
        #     self.leftIntake.setSpeed(.25)
        #     self.rightIntake.setSpeed(.25)
        # else:
        #     self.leftIntake.setSpeed(0)
        #     self.rightIntake.setSpeed(0)       
        
        if self.HMI.getX():
            self.leftIntake.setSpeed(-.35)     
            self.rightIntake.setSpeed(-.35)
        elif self.HMI.getB():
            self.leftIntake.setSpeed(.25)
            self.rightIntake.setSpeed(.25)
        else:
            self.leftIntake.setSpeed(0)
            self.rightIntake.setSpeed(0)

        # 1.) Poll position of Left X/Y and Right X/Y from controller
        Lx, Ly, Rx, _ = self.HMI.getAnalogSticks()

        # 2.) Move drivetrain based on Left X/Y and Right X/Y controller inputs
        self.SwerveDrive.move(Lx, Ly, Rx)


if __name__ == "__main__":
    wpilib.run(MyRobot)
