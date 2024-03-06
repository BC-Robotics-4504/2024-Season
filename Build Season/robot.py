import wpilib
from magicbot import MagicRobot

from components.config import RobotConfig

from components.hmi.hmi import HMI

from components.swerveDrive.swerveDrive import SwerveDrive, SparkMaxTurning, SparkMaxDriving
from components.swerveDrive.autoAlignment import AutoAlignment

from components.launcher.launcher import Launcher, SparkMaxDualSpinner, SparkMaxPivot
from components.launcher.launcherController import LauncherController

from components.climber.climber import Climber, SparkMaxClimb
from components.climber.climberController import ClimberController

from components.vision.limelight import Limelight
from components.vision.vision import Vision

class MyRobot(MagicRobot):

    # Configuration Class
    RobotConfig = RobotConfig()
    
    # Swerve Drive Component Code
    SwerveDrive: SwerveDrive
    
    # Controller Component Code
    HMI: HMI

    # Launcher Component Code
    Launcher: Launcher
    LauncherController: LauncherController

    # # Climber Component Code    
    # Climber: Climber
    # ClimberController: ClimberController

    # Vision Componenet Code
    Vision: Vision
    Alignment: AutoAlignment

    def createObjects(self):
        # Swerve Drive Hardware Config
        self.SwerveDrive_FrontLeftAngleMotor = SparkMaxTurning(6, inverted=False, gear_ratio=1, wheel_diameter=1, 
                                                               absolute_encoder=True, z_offset=-0.2)
        self.SwerveDrive_FrontLeftSpeedMotor = SparkMaxDriving(5, inverted=False, gear_ratio=1, wheel_diameter=0.1016)
        self.SwerveDrive_RearLeftAngleMotor = SparkMaxTurning(8, inverted=False, gear_ratio=1, wheel_diameter=1, 
                                                              absolute_encoder=True, z_offset=-0.35)
        self.SwerveDrive_RearLeftSpeedMotor = SparkMaxDriving(7, inverted=False, gear_ratio=1, wheel_diameter=0.1016)
        self.SwerveDrive_RearRightAngleMotor = SparkMaxTurning(2, inverted=False, gear_ratio=1, wheel_diameter=1, 
                                                               absolute_encoder=True, z_offset=-0.15)
        self.SwerveDrive_RearRightSpeedMotor = SparkMaxDriving(1, inverted=False, gear_ratio=1, wheel_diameter=0.1016)
        self.SwerveDrive_FrontRightAngleMotor = SparkMaxTurning(4, inverted=False, gear_ratio=1, wheel_diameter=1, 
                                                                absolute_encoder=True, z_offset=-0.25)
        self.SwerveDrive_FrontRightSpeedMotor = SparkMaxDriving(3, inverted=False, gear_ratio=1, wheel_diameter=0.1016)

        # Launcher Hardware Config
        self.Launcher_LauncherSpinnerL = SparkMaxDualSpinner(10, inverted=True)
        self.Launcher_LauncherSpinnerR = SparkMaxDualSpinner(12)

        self.Launcher_IntakeSpinnerL = SparkMaxDualSpinner(14, inverted=True)
        self.Launcher_IntakeSpinnerR = SparkMaxDualSpinner(13, inverted=True)

        self.Launcher_IntakePivot = SparkMaxPivot(9, inverted=False, gear_ratio=4, 
                                                  follower_canID=15)
        
        self.Launcher_LimitSwitch = wpilib.DigitalInput(0)
        
        # Climber Hardware Config
        # self.Climber_ClimberMotorL = SparkMaxClimb(14) #FIXME!!!
        # self.Climber_ClimberMotorR = SparkMaxClimb(15, inverted=True) #FIXME!!!

        # HMI Hardware Config
        self.HMI_xbox = wpilib.XboxController(0)

        # Vision Hardware Config
        self.Vision_LimeLight = Limelight() 
        self.Vision_LimeLightFront = Limelight(name='limelight-front')
               
        pass

    # def disabledPeriodic(self):
    #     pass

    def teleopInit(self):
        self.SwerveDrive.clearFaults()
        self.LauncherController.raiseIntake()
        pass

    def teleopPeriodic(self):
        print(self.Vision.getTargetDistance())
        # Move drivetrain based on Left X/Y and Right X/Y controller inputs
        Lx, Ly, Rx, _ = self.HMI.getAnalogSticks()

        self.SwerveDrive.move(Lx, Ly, Rx)

        # Actuate Launcher
        if self.HMI.getA():
            self.Vision.enableFrontCamera()
            self.LauncherController.lowerIntake()

        if self.HMI.getB():
            self.Vision.disableFrontCamera()
            self.LauncherController.raiseIntake()
            
        if self.HMI.getY():
            self.LauncherController.raiseIntakeAmp()
            
        if self.HMI.getRT() > 0.35:
            self.LauncherController.shootSpeaker()
            
        if self.HMI.getLT() > 0.35:
            self.Alignment.align()
                        
        # elif self.HMI.getLB():
        #     self.LauncherController.spindownLauncher()

        self.LauncherController.runLauncher()
        
        # #3.) Actuate Climber
        # if self.HMI.getRB():
        #     self.ClimberController.raiseClimber()

        # elif self.HMI.getLB():
        #     self.ClimberController.lowerClimber()

        # self.ClimberController.runClimber()

if __name__ == "__main__":
    wpilib.run(MyRobot)
