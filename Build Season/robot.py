import wpilib
from magicbot import MagicRobot

from components.swerveDrive.swerveDrive import SwerveModule, SwerveDrive, SparkMax, DriveConfig
from components.hmi.hmi import HMI

class MyRobot(MagicRobot):
    ''' MagicRobot Framework
    REFERENCE: https://robotpy.readthedocs.io/en/stable/frameworks/magicbot.html
    '''
    
    # Swerve Drive Component Code
    DriveConfig = DriveConfig(1.0, 1.0)
    SwerveDrive: SwerveDrive
    FrontLeft_SwerveModule: SwerveModule
    FrontRight_SwerveModule: SwerveModule
    RearLeft_SwerveModule: SwerveModule
    RearRight_SwerveModule: SwerveModule

    # Launcher Component Code

    # Climber Component Code    

    def createObjects(self):
        # Swerve Drive Hardware Config
        self.FrontLeft_SwerveModule_angleMotor = SparkMax(6, inverted=False, gear_ratio=1, wheel_diameter=1,
                                                          absolute_encoder=True)
        self.FrontLeft_SwerveModule_speedMotor = SparkMax(5, inverted=False, gear_ratio=1, wheel_diameter=1)

        self.FrontRight_SwerveModule_angleMotor = SparkMax(4, inverted=False, gear_ratio=1, wheel_diameter=1)
        self.FrontRight_SwerveModule_speedMotor = SparkMax(3, inverted=False, gear_ratio=1, wheel_diameter=1,
                                                          absolute_encoder=True)

        self.RearLeft_SwerveModule_angleMotor = SparkMax(8, inverted=False, gear_ratio=1, wheel_diameter=1)
        self.RearLeft_SwerveModule_speedMotor = SparkMax(7, inverted=False, gear_ratio=1, wheel_diameter=1,
                                                          absolute_encoder=True)

        self.RearRight_SwerveModule_angleMotor = SparkMax(2, inverted=False, gear_ratio=1, wheel_diameter=1)
        self.RearRight_SwerveModule_speedMotor = SparkMax(1, inverted=False, gear_ratio=1, wheel_diameter=1,
                                                          absolute_encoder=True)

        # Launcher Hardware Config

        # Climber Hardware Config

        # HMI Hardware Config
        self.HMI = HMI(controllerID=0)
        pass

    def disabledPeriodic(self):
        pass

    def teleopInit(self):
        # Define relationships between controller input events and what they're supposed to trigger
        # DO NOT PUT LEFT X/Y or RIGHT X/Y here--those will have to be updated using polling
        pass

    def teleopPeriodic(self):
        # 1.) Poll position of Left X/Y and Right X/Y from controller
        Lx, Ly, Rx, Ry = self.HMI.getAnalogSticks()

        # 2.) Move drivetrain based on Left X/Y and Right X/Y controller inputs
        self.SwerveDrive.move(Lx, Ly, Rx, Ry)


if __name__ == "__main__":
    wpilib.run(MyRobot)
