import math
from enum import Enum

import rev

from components.config import RobotConfig

class SparkMaxClimb:
    """Swerve Drive SparkMax Class
    Custom class for configuring SparkMaxes used in Climber mechanism 
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

        # Encoder parameters 
        # https://docs.reduxrobotics.com/canandcoder/spark-max
        # https://github.com/REVrobotics/MAXSwerve-Java-Template/blob/main/src/main/java/frc/robot/subsystems/MAXSwerveModule.java

        self.motor = rev.CANSparkMax(self.canID, rev.CANSparkMax.MotorType.kBrushless)  
        self.motor.restoreFactoryDefaults()
        self.motor.setInverted(not inverted)
        self.motor.setIdleMode(rev.CANSparkMax.IdleMode.kBrake)
        self.motor.setSmartCurrentLimit(25)

        self.SMcontroller = self.motor.getPIDController()
        self.encoder = self.motor.getAbsoluteEncoder(rev.SparkMaxAbsoluteEncoder.Type.kDutyCycle)
        self.encoder.setInverted(inverted)
        self.encoder.setPositionConversionFactor(2*math.pi)
        self.encoder.setVelocityConversionFactor(.104719755119659771)
        
        self.SMcontroller.setFeedbackDevice(self.encoder)
        self.SMcontroller.setPositionPIDWrappingEnabled(True) #TODO: does this need to be removed?
        self.SMcontroller.setPositionPIDWrappingMinInput(0) #TODO: does this need to be removed?
        self.SMcontroller.setPositionPIDWrappingMaxInput(2*math.pi) #TODO: does this need to be removed?
        
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
    
    def atPosition(self, tolerance=0.05):
        err = self.target_position - self.getPosition()
        if abs(err) <= tolerance:
            return True
        return False

class ClimberPositions(Enum):
    RAISED = 1
    LOWERING = 2
    LOWERED = 3
    RAISING = 4

class Climber:
    RobotConfig: RobotConfig

    ClimberMotorL: SparkMaxClimb
    ClimberMotorR: SparkMaxClimb

    ClimberPosition: ClimberPositions
    __climberChanged__: bool = False

    def __init__(self):
        self.ClimberPosition = ClimberPositions.LOWERED
        pass        

    def raiseClimber(self):  
        if self.ClimberPosition != ClimberPositions.RAISED:
            self.ClimberPosition = ClimberPositions.RAISING
            self.__climberChanged__ = True
        return None

    def lowerClimber(self):  
        if self.ClimberPosition != ClimberPositions.LOWERED:
            self.ClimberPosition = ClimberPositions.LOWERING
            self.__climberChanged__ = True
        return None

    def execute(self):
        if self.__climberChanged__:
            if self.ClimberPosition == ClimberPositions.LOWERING:
                self.ClimberMotorL.setPosition(0.0)
                self.ClimberMotorR.setPosition(0.0)
                atPositionL = self.ClimberMotorL.atPosition()
                atPositionR = self.ClimberMotorR.atPosition()
                if atPositionL and atPositionR:
                    self.ClimberPosition = ClimberPositions.LOWERED

            if self.ClimberPosition == ClimberPositions.RAISING:
                self.ClimberMotorL.setPosition(self.RobotConfig.climbing_max_distance)
                self.ClimberMotorR.setPosition(self.RobotConfig.climbing_max_distance)
                atPositionL = self.ClimberMotorL.atPosition()
                atPositionR = self.ClimberMotorR.atPosition()
                if atPositionL and atPositionR:
                    self.ClimberPosition = ClimberPositions.RAISED

