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
    Climber: Climber
    ClimberController: ClimberController

    # Vision Componenet Code
    Vision: Vision
    Alignment: AutoAlignment
    
    controlGain: float = 1

    def createObjects(self):
        """MyRobot.createObjects() -> None
        
        Create motors and other hardware components here."""
        # Swerve Drive Hardware Config
        self.SwerveDrive_FrontLeftAngleMotor = SparkMaxTurning(6, inverted=False, gear_ratio=1, wheel_diameter=1, 
                                                               absolute_encoder=True, z_offset=5.7535123)
        self.SwerveDrive_FrontLeftSpeedMotor = SparkMaxDriving(5, inverted=False, wheel_diameter=0.1143)
        self.SwerveDrive_RearLeftAngleMotor = SparkMaxTurning(8, inverted=False, wheel_diameter=1, 
                                                              absolute_encoder=True, z_offset=5.6867370)
        self.SwerveDrive_RearLeftSpeedMotor = SparkMaxDriving(7, inverted=False, wheel_diameter=0.1143)
        self.SwerveDrive_RearRightAngleMotor = SparkMaxTurning(2, inverted=False, wheel_diameter=1, 
                                                               absolute_encoder=True, z_offset=5.5975077)
        self.SwerveDrive_RearRightSpeedMotor = SparkMaxDriving(1, inverted=False, wheel_diameter=0.1143)
        self.SwerveDrive_FrontRightAngleMotor = SparkMaxTurning(4, inverted=False, wheel_diameter=1, 
                                                                absolute_encoder=True, z_offset=0.0182671)
        self.SwerveDrive_FrontRightSpeedMotor = SparkMaxDriving(3, inverted=False, wheel_diameter=0.1143)

        # Launcher Hardware Config
        self.Launcher_LauncherSpinnerL = SparkMaxDualSpinner(10, inverted=True)
        self.Launcher_LauncherSpinnerR = SparkMaxDualSpinner(12)

        self.Launcher_IntakeSpinnerL = SparkMaxDualSpinner(14, inverted=True)
        self.Launcher_IntakeSpinnerR = SparkMaxDualSpinner(13, inverted=True)

        self.Launcher_IntakePivot = SparkMaxPivot(9, inverted=False, gear_ratio=4, 
                                                  follower_canID=15)
        
        self.Launcher_LimitSwitch = wpilib.DigitalInput(0)
        
        #  Climber Hardware Config
        self.Climber_ClimberMotorL = SparkMaxClimb(16)
        self.Climber_ClimberMotorR = SparkMaxClimb(17, inverted=True)

        # HMI Hardware Config
        self.HMI_xbox = wpilib.XboxController(0)

        # Vision Hardware Config
        self.Vision_LimeLight = Limelight() 
        self.Vision_LimeLightFront = Limelight(name='limelight-front')
               
        pass

    # def disabledPeriodic(self):
    #     pass

    def teleopInit(self):
        """MyRobot.teleopInit() -> None
        
        Called once each time the robot enters teleoperated mode.
        """
        self.SwerveDrive.clearFaults()
        self.LauncherController.raiseIntake()
        pass

    def teleopPeriodic(self):
        """MyRobot.teleopPeriodic() -> None
        
        Called repeatedly during teleoperated mode."""
        # if self.Vision.getTargetDistance() is not None:
        #     print(self.Vision.getTargetDistance())
        # Move drivetrain based on Left X/Y and Right X/Y controller inputs
        Lx, Ly, Rx, _ = self.HMI.getAnalogSticks()
        
        # Rx *= self.controlGain
        Lx *= self.controlGain
        Ly *= self.controlGain

        self.SwerveDrive.move(Lx, Ly, Rx)

        # Actuate Launcher
        if self.HMI.getA():
            self.Vision.enableFrontCamera()
            self.LauncherController.lowerIntake()
            self.controlGain = -1

        if self.HMI.getB():
            self.Vision.disableFrontCamera()
            self.LauncherController.raiseIntake()
            self.controlGain = 1
            
        if self.HMI.getY():
            self.LauncherController.raiseIntakeAmp()
            
        if self.HMI.getRT() > 0.35:
            self.LauncherController.shootSpeaker()
            
        if self.HMI.getLT() > 0.35:
            self.Alignment.align()
        
        # #3.) Actuate Climber
        if self.HMI.getDpadUp():
            self.Climber.raiseClimber()
        
        elif self.HMI.getDpadDown():
            self.Climber.lowerClimber()
            
        elif self.HMI.getStart():
            self.Climber.lockClimber()
        
        #Runs LAUNCHER state machine
        self.LauncherController.runLauncher()
        '''
        SmartDashboard Setup
        '''
        # Add stuff to SmartDashboard
        wpilib.SmartDashboard.putNumber('LF Speed', self.SwerveDrive_FrontLeftSpeedMotor.getSpeed())
        wpilib.SmartDashboard.putNumber('LF Angle', self.SwerveDrive_FrontLeftAngleMotor.getAbsPosition())
        wpilib.SmartDashboard.putNumber('RF Speed', self.SwerveDrive_FrontRightSpeedMotor.getSpeed())
        wpilib.SmartDashboard.putNumber('RF Angle', self.SwerveDrive_FrontRightAngleMotor.getAbsPosition())
        wpilib.SmartDashboard.putNumber('LR Speed', self.SwerveDrive_RearLeftSpeedMotor.getSpeed())
        wpilib.SmartDashboard.putNumber('LR Angle', self.SwerveDrive_RearLeftAngleMotor.getAbsPosition())
        wpilib.SmartDashboard.putNumber('RR Speed', self.SwerveDrive_RearRightSpeedMotor.getSpeed())
        wpilib.SmartDashboard.putNumber('RR Angle', self.SwerveDrive_RearRightAngleMotor.getAbsPosition())

        wpilib.SmartDashboard.putNumberArray('L/R Flywheels', [self.Launcher.currentL_launcher_speed,
                                                               self.Launcher.currentR_launcher_speed])  
        
        wpilib.SmartDashboard.putBoolean('Shooting Camera Active', self.controlGain < 0)
        wpilib.SmartDashboard.putBoolean('Intake Camera Active', self.controlGain > 0)

        wpilib.SmartDashboard.putBoolean('Speaker In Range', self.Vision.inRange)
        
if __name__ == "__main__":
    wpilib.run(MyRobot)
