import math
from enum import Enum

import rev

from components.config import RobotConfig

class SparkMaxPivot:
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

        self.motor = rev.CANSparkMax(self.canID, rev.CANSparkMax.MotorType.kBrushless)  
        self.motor.restoreFactoryDefaults()
        self.motor.setInverted(not inverted)
        self.motor.setIdleMode(rev.CANSparkMax.IdleMode.kBrake)
        self.motor.setSmartCurrentLimit(25)

        self.SMcontroller = self.motor.getPIDController()
        self.encoder = self.motor.getEncoder()
        self.encoder.setInverted(inverted)
        self.encoder.setPositionConversionFactor(2*math.pi)
        self.encoder.setVelocityConversionFactor(.104719755119659771)
        
        self.SMcontroller.setFeedbackDevice(self.encoder)
        self.SMcontroller.setPositionPIDWrappingEnabled(False) #TODO: does this need to be removed?
        self.SMcontroller.setPositionPIDWrappingMinInput(0) #TODO: does this need to be removed?
        self.SMcontroller.setPositionPIDWrappingMaxInput(2*math.pi) #TODO: does this need to be removed?
        
        # PID parameters
        self.SMcontroller.setP(self.kP)
        self.SMcontroller.setI(self.kI)
        self.SMcontroller.setD(self.kD)
        self.SMcontroller.setIZone(self.kIz)
        self.SMcontroller.setFF(self.kFF)
        self.SMcontroller.setOutputRange(self.kMinOutput, self.kMaxOutput)

        # Smart Motion Parameters
        self.SMcontroller.setSmartMotionMaxVelocity(self.maxVel, self.smartMotionSlot)
        self.SMcontroller.setSmartMotionMinOutputVelocity(self.minVel, self.smartMotionSlot)
        self.SMcontroller.setSmartMotionMaxAccel(self.maxAcc, self.smartMotionSlot)
        self.SMcontroller.setSmartMotionAllowedClosedLoopError(self.allowedErr, self.smartMotionSlot)
        
        #self.controller.burnFlash()    
        self.clearFaults()
    
    def clearFaults(self):
        self.motor.clearFaults()
    
    def setPosition(self, position):
        self.target_position = position-self.zOffset
        self.SMcontroller.setReference(self.target_position, rev.CANSparkMax.ControlType.kPosition)
        return False
    
    def getPosition(self):
        rotation = self.encoder.getPosition()
        return rotation
    
    def atPosition(self, tolerance=0.05):
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
        self.encoder.setInverted(inverted)
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
        err = self.target_speed - self.getspeed()
        if abs(err) <= tolerance:
            return True
        return False
     
class IntakeLevelPositions(Enum):
    RAISED = 1
    LOWERING = 2
    LOWERED = 3
    RAISING = 4

class IntakeRollerPosiitons(Enum):
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
    IntakeSpinner: SparkMaxDualSpinner
    LauncherSpinner: SparkMaxDualSpinner

    IntakeLevelPosition: IntakeLevelPositions
    __intakeLevelChanged__: bool = False

    IntakeRollerPosiiton: IntakeRollerPosiitons 
    __intakeRollerChanged__: bool = False

    ShootingFlywheelPosition: ShootingFlywheelPositions
    __shootingFLywheelChanged__: bool = False

    def __init__(self):
        self.IntakeLevelPosition = IntakeLevelPositions.RAISED
        self.IntakeRollerPosiiton = IntakeRollerPosiitons.STOPPED
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
    
    def spinForward(self):
        if self.IntakeRollerPosiiton != IntakeRollerPosiitons.FORWARD:
            self.IntakeRollerPosiiton = IntakeRollerPosiitons.FORWARD
            self.__intakeRollerChanged__ = True
        return None
    
    def spinReverse(self):
        if self.IntakeRollerPosiiton != IntakeRollerPosiitons.REVERSE:
            self.IntakeRollerPosiiton = IntakeRollerPosiitons.REVERSE
            self.__intakeRollerChanged__ = True
        return None
    
    def spinStop(self):
        if self.IntakeRollerPosiiton != IntakeRollerPosiitons.STOPPED:
            self.IntakeRollerPosiiton = IntakeRollerPosiitons.STOPPED
            self.__intakeRollerChanged__ = False
        return None
    
    def spinupShooter(self):
        if self.ShootingFlywheelPosition != ShootingFlywheelPositions.RAMPING:
            self.ShootingFlywheelPosition = ShootingFlywheelPositions.RAMPING

    def execute(self):
        # Do intake level adjust work
        if self.__intakeLevelChanged__:
            if self.IntakePosition == IntakeLevelPositions.LOWERING:
                self.IntakePivot.setPosition(self.RobotConfig.intake_lowered_position)
                atPosition = self.IntakePivot.atPosition()
                if atPosition:
                    self.IntakePosition = IntakeLevelPositions.LOWERED

            if self.IntakePosition == IntakeLevelPositions.RAISING:
                self.IntakePivot.setPosition(self.RobotConfig.intake_raised_position)
                atPosition = self.IntakePivot.atPosition()
                if atPosition:
                    self.IntakePosition = IntakeLevelPositions.RAISED   

        # Do intake roller adjust work
        if self.__intakeRollerChanged__:
            if self.IntakeRollerPosiiton == IntakeRollerPosiitons.STOPPED:
                self.IntakeSpinner.setSpeed(0.0)

            if self.IntakeRollerPosiiton == IntakeRollerPosiitons.FORWARD:
                self.IntakeSpinner.setSpeed(self.RobotConfig.intake_forward_rolling_speed)

            if self.IntakeRollerPosiiton == IntakeRollerPosiitons.REVERSE:
                self.IntakeSpinner.setSpeed(self.RobotConfig.intake_reverse_rolling_speed)

        # Do intake flywheel adjust work
        if self.__shootingFLywheelChanged__:
            if self.ShootingFlywheelPosition == ShootingFlywheelPositions.RAMPING:
                self.LauncherSpinner.setSpeed(self.RobotConfig.shooting_flywheel_speed)
                atSpeed = self.LauncherSpinner.atSpeed()
                if atSpeed:
                    self.ShootingFlywheelPosition = ShootingFlywheelPositions.READY

            if self.ShootingFlywheelPosition == ShootingFlywheelPositions.STOPPING:
                self.LauncherSpinner.setSpeed(0.0)
                atSpeed = self.LauncherSpinner.atSpeed()
                if atSpeed:
                    self.ShootingFlywheelPosition = ShootingFlywheelPositions.STOPPED