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
    kP = 3
    kI = 1e-4
    kD = 1
    kIz = 0.30
    kFF = 0
    kMaxOutput = 1
    kMinOutput = -1
    maxRPM = 5700

    # Smart Motion Coefficients
    maxVel = 2000 # rpm
    maxAcc = 1500
    minVel = 0
    allowedErr = 0
    smartMotionSlot = 0

    target_position = 0

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
        
        self.SMcontroller.setSmartMotionMaxVelocity(self.maxVel, self.smartMotionSlot)
        self.SMcontroller.setSmartMotionMinOutputVelocity(self.minVel, self.smartMotionSlot)
        self.SMcontroller.setSmartMotionMaxAccel(self.maxAcc, self.smartMotionSlot)
        self.SMcontroller.setSmartMotionAllowedClosedLoopError(self.allowedErr, self.smartMotionSlot)
        
        # PID parameters
        self.SMcontroller.setP(self.kP)
        self.SMcontroller.setI(self.kI)
        self.SMcontroller.setD(self.kD)
        self.SMcontroller.setIZone(self.kIz)
        self.SMcontroller.setFF(self.kFF)
        self.SMcontroller.setOutputRange(self.kMinOutput, self.kMaxOutput)
    
    def clearFaults(self):
        self.motor.clearFaults()
    
    def setPosition(self, position):
        self.target_position = position-self.zOffset
        self.SMcontroller.setReference(self.target_position, rev.CANSparkMax.ControlType.kPosition)
        return False
    
    def getPosition(self):
        rotation = self.encoder.getPosition()
        return rotation
    
    def atPosition(self, tolerance=0.02):
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
        self.motor.clearFaults()
    
    def setSpeed(self, speed):
        self.target_speed = speed
        self.motor.set(speed)
        return False
    
    def getSpeed(self):
        return self.encoder.getVelocity()
    
    def atSpeed(self, tolerance=0.05):
        err = self.target_speed - self.getSpeed()
        if abs(err) <= tolerance:
            return True
        return False
     
class IntakeLevelPositions(Enum):
    RAISED = 1
    LOWERING = 2
    LOWERED = 3
    RAISING = 4

class IntakeRollerPositions(Enum):
    STOPPED = 1
    FORWARD = 2
    REVERSE = 3

class ShootingFlywheelPositions(Enum):
    STOPPED = 1
    RAMPING = 2
    READY = 3
    STOPPING = 4

class Launcher:
    RobotConfig: RobotConfig

    IntakePivot: SparkMaxPivot

    IntakeSpinnerL: SparkMaxDualSpinner
    IntakeSpinnerR: SparkMaxDualSpinner

    LauncherSpinnerL: SparkMaxDualSpinner
    LauncherSpinnerR: SparkMaxDualSpinner

    IntakeLevelPosition: IntakeLevelPositions
    __intakeLevelChanged__: bool = False

    IntakeRollerPosition: IntakeRollerPositions 
    __intakeRollerChanged__: bool = False

    ShootingFlywheelPosition: ShootingFlywheelPositions
    __shootingFLywheelChanged__: bool = False
    __shootingFLywheelSpeed__: float = 0.0
    
    LimitSwitch: wpilib.DigitalInput

    def __init__(self):
        self.IntakeLevelPosition = IntakeLevelPositions.RAISED
        self.IntakeRollerPosition = IntakeRollerPositions.STOPPED
        self.ShootingFlywheelPosition = ShootingFlywheelPositions.STOPPED
        pass

    def lowerIntake(self):  
        if self.IntakeLevelPosition != IntakeLevelPositions.LOWERING:
            self.IntakeLevelPosition = IntakeLevelPositions.LOWERING 
            self.__intakeLevelChanged__ = True
        return None

    def retractIntake(self):
        if self.IntakeLevelPosition != IntakeLevelPositions.RAISING:
            self.IntakeLevelPosition = IntakeLevelPositions.RAISING  
            self.__intakeLevelChanged__ = True   

        return None
    
    def spinIntakeForward(self):
        if self.IntakeRollerPosition != IntakeRollerPositions.FORWARD:
            self.IntakeRollerPosition = IntakeRollerPositions.FORWARD
            self.__intakeRollerChanged__ = True
        return None
    
    def spinIntakeReverse(self):
        if self.IntakeRollerPosition != IntakeRollerPositions.REVERSE:
            self.IntakeRollerPosition = IntakeRollerPositions.REVERSE
            self.__intakeRollerChanged__ = True
        return None
    
    def spindownIntake(self):
        if self.IntakeRollerPosition != IntakeRollerPositions.STOPPED:
            self.IntakeRollerPosition = IntakeRollerPositions.STOPPED
            self.__intakeRollerChanged__ = True
        return None
    
    def spinupShooter(self, speed):
        if self.ShootingFlywheelPosition != ShootingFlywheelPositions.RAMPING:
            self.ShootingFlywheelPosition = ShootingFlywheelPositions.RAMPING
            self.__shootingFLywheelSpeed__ = speed
            self.__shootingFLywheelChanged__ = True
        return None

    def spindownShooter(self):
        if self.ShootingFlywheelPosition != ShootingFlywheelPositions.STOPPING:
            self.ShootingFlywheelPosition = ShootingFlywheelPositions.STOPPING  
            self.__shootingFLywheelSpeed__ = 0
            self.__shootingFLywheelChanged__ = True  
        return None  

    def __updateIntakeRollers__(self):
        if self.__intakeRollerChanged__:
            if self.IntakeRollerPosition == IntakeRollerPositions.STOPPED:
                self.IntakeSpinnerL.setSpeed(0.0)
                self.IntakeSpinnerR.setSpeed(0.0)

            if self.IntakeRollerPosition == IntakeRollerPositions.FORWARD:
                self.IntakeSpinnerL.setSpeed(self.RobotConfig.intake_forward_rolling_speed)
                self.IntakeSpinnerR.setSpeed(self.RobotConfig.intake_forward_rolling_speed)
                atSpeedL = self.IntakeSpinnerL.atSpeed()
                atSpeedR = self.IntakeSpinnerR.atSpeed()
                if atSpeedL and atSpeedR:
                    self.IntakeRollerPosition = IntakeRollerPositions.FORWARD

            if self.IntakeRollerPosition == IntakeRollerPositions.REVERSE:
                self.IntakeSpinnerL.setSpeed(self.RobotConfig.intake_reverse_rolling_speed)
                self.IntakeSpinnerR.setSpeed(self.RobotConfig.intake_reverse_rolling_speed)
                atSpeedL = self.IntakeSpinnerL.atSpeed()
                atSpeedR = self.IntakeSpinnerR.atSpeed()
                if atSpeedL and atSpeedR:
                    self.IntakeRollerPosition = IntakeRollerPositions.REVERSE

            self.__intakeRollerChanged__ = False
            
        if not self.LimitSwitch.get():
            self.IntakeSpinnerL.setSpeed(0.0)
            self.IntakeSpinnerR.setSpeed(0.0)     
            self.IntakeRollerPosition = IntakeRollerPositions.STOPPED   
               

        return None
    
    def __updateIntakeLevel__(self):
        # Do intake level adjust work
        # if self.__intakeLevelChanged__:
        if self.IntakeLevelPosition == IntakeLevelPositions.LOWERING:
            self.IntakePivot.setPosition(self.RobotConfig.intake_lowered_position)
            atPosition = self.IntakePivot.atPosition()
            if atPosition:
                self.IntakeLevelPosition = IntakeLevelPositions.LOWERED

        if self.IntakeLevelPosition == IntakeLevelPositions.RAISING:
            self.IntakePivot.setPosition(self.RobotConfig.intake_raised_position)
            atPosition = self.IntakePivot.atPosition()
            if atPosition:
                self.IntakeLevelPosition = IntakeLevelPositions.RAISED   
        return None
    
    def __updateFlywheels__(self):
        
        if self.__shootingFLywheelChanged__:

            if self.ShootingFlywheelPosition == ShootingFlywheelPositions.RAMPING:
                self.LauncherSpinnerL.setSpeed(self.__shootingFLywheelSpeed__)
                self.LauncherSpinnerR.setSpeed(self.__shootingFLywheelSpeed__)
                # atSpeedL = self.LauncherSpinnerL.atSpeed()
                # atSpeedR = self.LauncherSpinnerR.atSpeed()
                # if atSpeedL and atSpeedR:
                self.ShootingFlywheelPosition = ShootingFlywheelPositions.READY

            if self.ShootingFlywheelPosition == ShootingFlywheelPositions.STOPPING:
                self.LauncherSpinnerL.setSpeed(0.0)
                self.LauncherSpinnerR.setSpeed(0.0)
                # atSpeedL = self.LauncherSpinnerL.atSpeed()
                # atSpeedR = self.LauncherSpinnerR.atSpeed()
                # if atSpeedL and atSpeedR:
                self.ShootingFlywheelPosition = ShootingFlywheelPositions.STOPPED
                
        return None

    def execute(self):
        # Do intake level adjust work
        self.__updateIntakeLevel__()

        # Do intake roller adjust work
        self.__updateIntakeRollers__()

        # Do intake flywheel adjust work
        self.__updateFlywheels__()

