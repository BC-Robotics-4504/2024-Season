import math
from enum import Enum

import rev

from components.config import RobotConfig

class SparkMaxClimb:
    """Swerve Drive SparkMax Class
    Custom class for configuring SparkMaxes used in Climber mechanism 
    """
    
    # PID coefficients
    kP = 5e-3
    kI = 5e-8
    kD = 0
    kIz = 0
    kFF = 0
    kMaxOutput = 2500
    kMinOutput = -2500
    maxRPM = 2500

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
        self.motor.setSmartCurrentLimit(60)

        self.SMcontroller = self.motor.getPIDController()
        self.encoder = self.motor.getEncoder()
        self.encoder.setPosition(0)
        self.encoder.setPositionConversionFactor(1)
        self.encoder.setVelocityConversionFactor(1)
        
        # self.SMcontroller.setPositionPIDWrappingEnabled(True) #TODO: does this need to be removed?
        # self.SMcontroller.setPositionPIDWrappingMinInput(0) #TODO: does this need to be removed?
        # self.SMcontroller.setPositionPIDWrappingMaxInput(1) #TODO: does this need to be removed?
        
        # PID parameters
        self.SMcontroller.setP(self.kP, slotID=0)
        self.SMcontroller.setI(self.kI, slotID=0)
        self.SMcontroller.setD(self.kD, slotID=0)
        self.SMcontroller.setIZone(self.kIz, slotID=0)
        self.SMcontroller.setFF(self.kFF, slotID=0)
        self.SMcontroller.setOutputRange(self.kMinOutput, self.kMaxOutput, slotID=0)
    
    def clearFaults(self):
        """SparkMaxClimb.clearFaults() -> None
        
        Clear any faults on the motor controller."""
        self.motor.clearFaults()
    
    def setPosition(self, position : float):
        """SparkMaxClimb.setPosition(position: float) -> None
        
        Set the position of the motor controller.
        
        ::params:
        position:position to set the motor controller to
        
        """
        self.target_position = position
        self.SMcontroller.setReference(self.target_position, rev.CANSparkMax.ControlType.kPosition)
        return False
    
    def getPosition(self):
        """SparkMaxClimb.getPosition() -> float
        
        Get the position of the motor controller."""
        
        rotation = self.encoder.getPosition()
        return rotation
    
    def atPosition(self, tolerance=0.05):
        """SparkMaxClimb.atPosition(tolerance: float) -> bool
        
        See if the motor controller is at the target position.
        """
        err = self.target_position - self.getPosition()
        if abs(err) <= tolerance:
            return True
        return False
    
class ClimberState(Enum):
    LOWERED = 1
    RAISED = 2
    LOCKED = 3

class Climber:
    RobotConfig: RobotConfig

    ClimberMotorL: SparkMaxClimb
    ClimberMotorR: SparkMaxClimb

    __climberChanged__: bool = False  
    
    climber_state = ClimberState.RAISED  
    
    def lockClimber(self):
        
        if self.isLocked():
            return None
        
        rotations = self.RobotConfig.climber_position_locked/self.RobotConfig.climbing_m_per_rot
        self.ClimberMotorL.setPosition(rotations)
        self.ClimberMotorR.setPosition(rotations)
        
        self.climber_state = ClimberState.LOCKED
        return False
    
    def isLocked(self):
        if self.climber_state == ClimberState.LOCKED:
            return True
        return False

    def raiseClimber(self):
        """Climber.raiseClimber() -> None
        
        Raise the climber."""  
        
        if self.isLocked():
            return None
        
        if self.climber_state != ClimberState.RAISED:
            rotations = self.RobotConfig.climber_position_raised/self.RobotConfig.climbing_m_per_rot
            self.ClimberMotorL.setPosition(-rotations)
            self.ClimberMotorR.setPosition(-rotations)
            self.climber_state = ClimberState.RAISED
        return None

    def lowerClimber(self):  
        """Climber.lowerClimber() -> None
        
        Lower the climber."""
        
        if self.isLocked():
            return None
        
        if self.climber_state != ClimberState.LOWERED:
            rotations = self.RobotConfig.climber_position_low/self.RobotConfig.climbing_m_per_rot
            # print(rotations, self.RobotConfig., self.RobotConfig.climbing_m_per_rot)
            self.ClimberMotorL.setPosition(rotations)
            self.ClimberMotorR.setPosition(rotations)
            self.climber_state = ClimberState.LOWERED
        return None

    def execute(self):
        """Climber.execute() -> None
        
        Execute the climber commands."""
        self.leftArmPosition = self.ClimberMotorL.getPosition()
        self.rightArmPosition = self.ClimberMotorR.getPosition()

