import wpilib
from magicbot import MagicRobot

from components.swerveDrive.swerveDrive import SwerveModule, SwerveDrive, SparkMaxTurning, SparkMaxDriving, DriveConfig
from components.hmi.hmi import HMI

class MyRobot(MagicRobot):
    ''' MagicRobot Framework
    REFERENCE: https://robotpy.readthedocs.io/en/stable/frameworks/magicbot.html
    '''
    
    # Swerve Drive Component Code
    DriveConfig = DriveConfig(34.0, 34.0)
    SwerveDrive: SwerveDrive
    FrontLeft_SwerveModule: SwerveModule
    FrontRight_SwerveModule: SwerveModule
    RearLeft_SwerveModule: SwerveModule
    RearRight_SwerveModule: SwerveModule
    
    # Controller Component Code
    HMI: HMI

    # Launcher Component Code

    # Climber Component Code    

    def createObjects(self):
        # Swerve Drive Hardware Config
        self.FrontLeft_SwerveModule_angleMotor = SparkMaxTurning(6, inverted=False, gear_ratio=1, wheel_diameter=1,
                                                          absolute_encoder=True)
        self.FrontLeft_SwerveModule_speedMotor = SparkMaxDriving(5, inverted=False, gear_ratio=1, wheel_diameter=1)

        self.FrontRight_SwerveModule_angleMotor = SparkMaxTurning(4, inverted=False, gear_ratio=1, wheel_diameter=1,
                                                          absolute_encoder=True)
        self.FrontRight_SwerveModule_speedMotor = SparkMaxDriving(3, inverted=False, gear_ratio=1, wheel_diameter=1)

        self.RearLeft_SwerveModule_angleMotor = SparkMaxTurning(8, inverted=True, gear_ratio=1, wheel_diameter=1,
                                                          absolute_encoder=True)
        self.RearLeft_SwerveModule_speedMotor = SparkMaxDriving(7, inverted=False, gear_ratio=1, wheel_diameter=1)

        self.RearRight_SwerveModule_angleMotor = SparkMaxTurning(2, inverted=False, gear_ratio=1, wheel_diameter=1,
                                                          absolute_encoder=True)
        self.RearRight_SwerveModule_speedMotor = SparkMaxDriving(1, inverted=False, gear_ratio=1, wheel_diameter=1)

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
        self.SwerveDriveFaults()
        pass

    def teleopPeriodic(self):
        # 1.) Poll position of Left X/Y and Right X/Y from controller
        Lx, Ly, Rx, Ry = self.HMI.getAnalogSticks()
        print(self.HMI.getAnalogSticks)
        
        # 2.) Move drivetrain based on Left X/Y and Right X/Y controller inputs
        self.SwerveDrive.move(Lx, Ly, Rx, Ry)


if __name__ == "__main__":
    wpilib.run(MyRobot)
