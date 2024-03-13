import math
from enum import Enum

import wpilib
import rev

from components.config import RobotConfig

class SparkMaxPivot:
    """Swerve Drive SparkMax Class
    Custom class for configuring SparkMaxes used in Swerve Drive Drivetrain
    """
    
    # PID coefficients
    kP = 0.9
    kI = 0
    kD = 0
    kIz = 0.
    kFF = 0
    kMaxOutput = 1
    kMinOutput = -1
    maxRPM = 5700

    # Smart Motion Coefficients
    maxVel = 2000 # rpm
    maxAcc = 1500
    minVel = 0
    allowedErr = 0.01
    smartMotionSlot = 0

    target_position = 0

    def __init__(
        self,
        canID,
        inverted=False,
        gear_ratio=1,
        wheel_diameter=1,
        absolute_encoder=False,
        z_offset = 0,
        follower_canID = None,
    ):
        self.canID = canID
        self.follower_canID = follower_canID
        self.gear_ratio = gear_ratio
        self.inverted = inverted
        self.absolute = absolute_encoder
        self.gear_ratio = gear_ratio
        self.wheel_diameter = wheel_diameter
        self.zOffset = z_offset

        # Encoder parameters 
        # https://docs.reduxrobotics.com/canandcoder/spark-max
        # https://github.com/REVrobotics/MAXSwerve-Java-Template/blob/main/src/main/java/frc/robot/subsystems/MAXSwerveModule.java

        self.motor = rev.CANSparkMax(self.canID, rev.CANSparkMax.MotorType.kBrushless)  
        self.motor.restoreFactoryDefaults()
        self.motor.setInverted(inverted)
        self.motor.setIdleMode(rev.CANSparkMax.IdleMode.kBrake)
        self.motor.setSmartCurrentLimit(40)

        self.SMcontroller = self.motor.getPIDController()
        self.encoder = self.motor.getAbsoluteEncoder(rev.SparkMaxAbsoluteEncoder.Type.kDutyCycle)
        self.encoder.setInverted(inverted)
        self.encoder.setPositionConversionFactor(2*math.pi/self.gear_ratio)
        self.encoder.setVelocityConversionFactor(.104719755119659771)
        
        self.SMcontroller.setFeedbackDevice(self.encoder)
        self.SMcontroller.setPositionPIDWrappingEnabled(False) #TODO: does this need to be removed?
        self.SMcontroller.setPositionPIDWrappingMinInput(0) #TODO: does this need to be removed?
        self.SMcontroller.setPositionPIDWrappingMaxInput(2*math.pi/self.gear_ratio) #TODO: does this need to be removed?
        
        # self.SMcontroller.setSmartMotionMaxVelocity(self.maxVel, self.smartMotionSlot)
        # self.SMcontroller.setSmartMotionMinOutputVelocity(self.minVel, self.smartMotionSlot)
        # self.SMcontroller.setSmartMotionMaxAccel(self.maxAcc, self.smartMotionSlot)
        # self.SMcontroller.setSmartMotionAllowedClosedLoopError(self.allowedErr, self.smartMotionSlot)
        
        # PID parameters
        self.SMcontroller.setP(self.kP)
        self.SMcontroller.setI(self.kI)
        self.SMcontroller.setD(self.kD)
        self.SMcontroller.setIZone(self.kIz)
        self.SMcontroller.setFF(self.kFF)
        self.SMcontroller.setOutputRange(self.kMinOutput, self.kMaxOutput)
        
        # Setup follower
        if follower_canID is not None:
            follower_motor = rev.CANSparkMax(self.follower_canID, rev.CANSparkMax.MotorType.kBrushless) 
            follower_motor.restoreFactoryDefaults()
            # follower_motor.setIdleMode(rev.CANSparkMax.IdleMode.kCoast)
            # follower_motor.setSmartCurrentLimit(40)
            follower_motor.follow(self.motor, invert=True)
            
            self.follower_motor = follower_motor
            
        else:
            self.follower_motor = None
    
    def clearFaults(self):
        """SparkMaxPivot.clearFaults() -> None
        
        Clear the faults on the motor controller."""
        self.motor.clearFaults()
    
    def setPosition(self, position):
        """SparkMaxPivot.setPosition(position: float) -> None
        
        Set the position of the motor controller.
        
        ::params:
        position: float : The position to set the motor controller to."""
        self.target_position = position-self.zOffset
        self.SMcontroller.setReference(self.target_position, rev.CANSparkMax.ControlType.kPosition)
        return False
    
    def getPosition(self):
        """SparkMaxPivot.getPosition() -> float
        
        Get the position of the motor controller."""
        rotation = self.encoder.getPosition()
        return rotation
    
    def atPosition(self, tolerance=0.05):
        """SparkMaxPivot.atPosition(tolerance: float) -> bool
        
        Check if the motor controller is at the target position."""
        err = self.target_position - self.getPosition()
        if abs(err) <= tolerance:
            return True
        return False
        
    
class SparkMaxDualSpinner:
    """Swerve Drive SparkMax Class
    Custom class for configuring SparkMaxes used in Swerve Drive Drivetrain
    """
    
    # PID coefficients
    kP = 0.32
    kI = 1e-4
    kD = 1
    kIz = 0.30
    kFF = 0
    kMaxOutput = 1
    kMinOutput = -1
    maxRPM = 5700

    # Smart Motion Coefficients
    maxVel = 2000  # rpm
    maxAcc = 1000
    minVel = 0
    allowedErr = 0

    smartMotionSlot=0

    def __init__(
        self,
        canID,
        inverted=False,
        gear_ratio=1,
        wheel_diameter=1,
        absolute_encoder=False,
        z_offset = 0
    ):
        self.canID = canID
        self.gear_ratio = gear_ratio
        self.inverted = inverted
        self.absolute = absolute_encoder
        self.gear_ratio = gear_ratio
        self.wheel_diameter = wheel_diameter
        self.zOffset = z_offset

        self.motor = rev.CANSparkMax(self.canID, rev.CANSparkMax.MotorType.kBrushless)  
        self.motor.restoreFactoryDefaults()
        self.motor.setInverted(not inverted)
        self.motor.setIdleMode(rev.CANSparkMax.IdleMode.kBrake)
        self.motor.setSmartCurrentLimit(25)

        self.SMcontroller = self.motor.getPIDController()
        self.encoder = self.motor.getEncoder()
        # self.encoder.setInverted(inverted)
        self.encoder.setVelocityConversionFactor(.104719755119659771)
        
        #self.controller.burnFlash()    
        self.clearFaults()
    
    def clearFaults(self):
        """SparkMaxDualSpinner.clearFaults() -> None
        
        Clear the faults on the motor controller."""
        self.motor.clearFaults()
    
    def setSpeed(self, speed):
        """SparkMaxDualSpinner.setSpeed(speed: float) -> None
        
        Set the speed of the motor controller.
        
        ::params:
        speed: float : The speed to set the motor controller to."""
    
        self.target_speed = speed
        self.motor.set(speed)
        return False
    
    def getSpeed(self):
        """SparkMaxDualSpinner.getSpeed() -> float
        
        Gets the current speed of the motor controller."""
        return self.encoder.getVelocity()
    
    def atSpeed(self, tolerance=0.02):
        """SparkMaxDualSpinner.atSpeed(tolerance: float) -> bool
        
        Check if the motor controller is at speed."""
        err = self.target_speed - self.getSpeed()
        if abs(err) <= tolerance:
            return True
        return False
    
class Launcher:
    RobotConfig: RobotConfig

    IntakePivot: SparkMaxPivot

    IntakeSpinnerL: SparkMaxDualSpinner
    IntakeSpinnerR: SparkMaxDualSpinner

    LauncherSpinnerL: SparkMaxDualSpinner
    LauncherSpinnerR: SparkMaxDualSpinner

    LimitSwitch: wpilib.DigitalInput
    
    current_intake_position = None
    target_intake_position = None
    
    currentL_launcher_speed = 0
    currentR_launcher_speed = 0
    target_launcher_speed = 0

    def __init__(self):
        pass
    
    def isPositionedIntake(self):
        """Launcher.isPositionedIntake() -> bool
        
        Check if the intake is in the correct postition."""
        if self.target_intake_position is None:
            return False
        
        err = self.current_intake_position - self.target_intake_position
        if abs(err) < self.RobotConfig.intake_tolerance:
            return True
        return False 
    
    def isNoteInIntake(self):
        """Launcher.isNoteInIntake() -> bool
        
        Check if a note is in the intake."""
        note_in_intake = not self.LimitSwitch.get()
        is_lowered = self.target_intake_position == self.RobotConfig.intake_lowered_position
        if is_lowered and note_in_intake:
            return True
        return False
    
    def lowerIntake(self):  
        """Launcher.lowerIntake() -> None
        
        Lower the intake."""
        self.target_intake_position = self.RobotConfig.intake_lowered_position
        self.IntakePivot.setPosition(self.RobotConfig.intake_lowered_position)
        return None      
    
    def raiseIntake(self):
        """Launcher.raiseIntake() -> None
        
        Raise the intake."""
        self.target_intake_position = self.RobotConfig.intake_raised_position
        self.IntakePivot.setPosition(self.RobotConfig.intake_raised_position)   
        return None
    
    def isLauncherAtSpeed(self):
        """Launcher.isLauncherAtSpeed() -> bool
        
        Check if the launcher is at speed."""
        errL = self.currentL_launcher_speed > self.RobotConfig.shooting_flywheel_threshold_speed
        errR = self.currentR_launcher_speed > self.RobotConfig.shooting_flywheel_threshold_speed
        if errL and errR:
            return True
        return False
    
    def spinupShooter(self):
        """Launcher.spinupShooter() -> None
        
        Spin the launcher up."""
        self.LauncherSpinnerL.setSpeed(self.RobotConfig.shooting_flywheel_speed)
        self.LauncherSpinnerR.setSpeed(self.RobotConfig.shooting_flywheel_speed)
        return None
    
    def spindownLauncher(self):
        """Launcher.spindownLauncher() -> None
        
        Spin the launcher down."""
        self.LauncherSpinnerL.setSpeed(0.0)
        self.LauncherSpinnerR.setSpeed(0.0)  
        return None  
    
    def feedShooterSpeaker(self):
        """Launcher.feedShooterSpeaker() -> None
        
        Feed the shooter when shooter is spinning up to shoot speaker."""
        self.IntakeSpinnerL.setSpeed(self.RobotConfig.intake_feed_speaker_speed)
        self.IntakeSpinnerR.setSpeed(self.RobotConfig.intake_feed_speaker_speed) 
        return None   
    
    def spindownIntake(self):
        """Launcher.spindownIntake() -> None
        
        Spin the intake down."""
        self.IntakeSpinnerL.setSpeed(0.0)
        self.IntakeSpinnerR.setSpeed(0.0)
        return None
    
    #def spindownIntake(self): #! Duplicate method
    #     self.IntakeSpinnerL.setSpeed(0.0)
    #     self.IntakeSpinnerR.setSpeed(0.0)
    #     return None    
    
    def spinIntakeIn(self):
        """Launcher.spinIntakeIn() -> None
        
        Spin the intake in."""
        self.IntakeSpinnerL.setSpeed(self.RobotConfig.intake_reverse_rolling_speed)
        self.IntakeSpinnerR.setSpeed(self.RobotConfig.intake_reverse_rolling_speed)
        return None
    
    def ampIntake(self):
        """Launcher.ampIntake() -> None
        
        Raise the intake to the amp position."""
        self.target_intake_position = self.RobotConfig.intake_amp_position
        self.IntakePivot.setPosition(self.RobotConfig.intake_amp_position)
        return None
    
    def feedShooterAmp(self):
        """Launcher.feedShooterAmp() -> None
        
        Feed the shooter when shooter is spinning up to shoot amp."""
        self.IntakeSpinnerL.setSpeed(self.RobotConfig.intake_amp_shooting_speed+0.02)
        self.IntakeSpinnerR.setSpeed(self.RobotConfig.intake_amp_shooting_speed) 
        return None
    
    def execute(self):
        """Launcher.execute() -> None
        
        Updates position and speed of the Launcher."""
        self.current_intake_position = self.IntakePivot.getPosition()
        self.currentL_launcher_speed = self.LauncherSpinnerL.getSpeed()
        self.currentR_launcher_speed = self.LauncherSpinnerR.getSpeed()      
        pass