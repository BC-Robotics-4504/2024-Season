from wpimath.geometry import Translation2d, Rotation2d
from wpimath.kinematics import SwerveDrive4Kinematics, ChassisSpeeds, SwerveModuleState
from wpimath.estimator import SwerveDrive4PoseEstimator

import math
from dataclasses import dataclass  # * Why do we need this import statement?
import rev

# Drivetrain configuration parameters
@dataclass
class DriveConfig:
    """Drivetrain Configuration
    Custom class for configuring SparkMaxes used in Swerve Drive Drivetrain
    REFERENCE: https://docs.python.org/3/library/dataclasses.html
    """

    chasis_length: float
    chasis_width: float
    speed_clamp: float = 0.1

    @property
    def ratio(self):
        return math.hypot(self.chasis_length, self.chasis_width/2)

    @property
    def frontLeftLocation(self):
        return Translation2d(self.chasis_length/2, self.chasis_width/2)
    
    @property
    def frontRightLocation(self):
        return Translation2d(self.chasis_length/2, -self.chasis_width/2)
    
    @property
    def backLeftLocation(self):
        return Translation2d(-self.chasis_length/2, self.chasis_width/2)

    @property
    def backRightLocation(self):
        return Translation2d(-self.chasis_length/2, -self.chasis_width/2)  

class SparkMaxTurning:
    """Swerve Drive SparkMax Class
    Custom class for configuring SparkMaxes used in Swerve Drive Drivetrain
    """
    
    # PID coefficients
    kP = 1e-5
    kI = 1e-8
    kD = 0
    kIz = 0
    # kFF = 0.000156
    kFF = 0.0005
    kMaxOutput = 1
    kMinOutput = 0
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
    ):
        self.canID = canID
        self.gear_ratio = gear_ratio
        self.inverted = inverted
        self.absolute = absolute_encoder
        self.gear_ratio = gear_ratio
        self.wheel_diameter = wheel_diameter

        # Encoder parameters 
        # https://docs.reduxrobotics.com/canandcoder/spark-max
        # https://github.com/REVrobotics/MAXSwerve-Java-Template/blob/main/src/main/java/frc/robot/subsystems/MAXSwerveModule.java

        self.motor = rev.CANSparkMax(canID, rev.CANSparkMax.MotorType.kBrushless)  
        self.motor.restoreFactoryDefaults()
        self.motor.setInverted(inverted) #TODO: does this need to be removed?                 
        self.motor.setIdleMode(rev.CANSparkMax.IdleMode.kBrake)
        self.motor.setSmartCurrentLimit(25)

        self.controller = self.motor.getPIDController()
        self.encoder = self.motor.getAbsoluteEncoder(rev.SparkAbsoluteEncoder.Type.kDutyCycle)
        # self.encoder.setAverageDepth(1)
        # self.encoder.setZeroOffset(0)
        # self.encoder.setInverted(False)
        # self.encoder.setPositionConversionFactor(1.0)
        # self.encoder.setVelocityConversionFactor(1.0)
        self.controller.setFeedbackDevice(self.encoder)
        
        # self.encoder.setPositionConversionFactor(1.0)
        # self.encoder.setVelocityConversionFactor(1.0)
        # self.controller.setPositionPIDWrappingEnabled(True) #TODO: does this need to be removed?
        # self.controller.setPositionPIDWrappingMinInput(0) #TODO: does this need to be removed?
        # self.controller.setPositionPIDWrappingMaxInput(1) #TODO: does this need to be removed?
        
        # PID parameters
        self.controller.setP(self.kP)
        self.controller.setI(self.kI)
        self.controller.setD(self.kD)
        self.controller.setIZone(self.kIz)
        self.controller.setFF(self.kFF)
        self.controller.setOutputRange(self.kMinOutput, self.kMaxOutput)
        self.controller.setOutputRange()

        # Smart Motion Parameters
        self.controller.setSmartMotionMaxVelocity(self.maxVel, self.smartMotionSlot)
        self.controller.setSmartMotionMinOutputVelocity(self.minVel, self.smartMotionSlot)
        self.controller.setSmartMotionMaxAccel(self.maxAcc, self.smartMotionSlot)
        self.controller.setSmartMotionAllowedClosedLoopError(self.allowedErr, self.smartMotionSlot)
        
        #self.controller.burnFlash()    
        self.clearFaults()
    
    def clearFaults(self):
        self.motor.clearFaults()
    
    def setAbsPosition(self, position):
        self.controller.setReference(position, rev.CANSparkMax.ControlType.kDutyCycle)
        return False
    
    def getAbsPosition(self):
        rotation = self.encoder.getPosition()
        return rotation

class SparkMaxDriving:
    """Swerve Drive SparkMax Class
    Custom class for configuring SparkMaxes used in Swerve Drive Drivetrain
    """
    
    # PID coefficients
    kP = 0.04
    kI = 0
    kD = 0
    kIz = 0
    kFF = 1
    kMaxOutput = 1
    kMinOutput = -1
    maxRPM = 5700

    # Smart Motion Coefficients
    maxVel = 2000  # rpm
    maxAcc = 1000
    minVel = 0
    allowedErr = 0

    def __init__(
        self,
        canID,
        inverted=False,
        gear_ratio=1,
        wheel_diameter=1,
        absolute_encoder=False,
    ):
        self.canID = canID
        self.gear_ratio = gear_ratio
        self.inverted = inverted
        self.absolute = absolute_encoder
        self.gear_ratio = gear_ratio
        self.wheel_diameter = wheel_diameter

        # Encoder parameters 
        # https://docs.reduxrobotics.com/canandcoder/spark-max
        # https://github.com/REVrobotics/MAXSwerve-Java-Template/blob/main/src/main/java/frc/robot/subsystems/MAXSwerveModule.java

        self.motor = rev.CANSparkMax(canID, rev.CANSparkMax.MotorType.kBrushless)  
        self.motor.restoreFactoryDefaults()
         
        self.encoder = self.motor.getEncoder()
        self.controller = self.motor.getPIDController()
        self.controller.setFeedbackDevice(self.encoder)
        
        self.encoder.setPositionConversionFactor(1)
        self.encoder.setVelocityConversionFactor(1)
        
        # PID parameters
        self.controller.setP(self.kP)
        self.controller.setI(self.kI)
        self.controller.setD(self.kD)
        self.controller.setFF(self.kFF)
        self.controller.setOutputRange(self.kMinOutput, self.kMaxOutput)
        
        self.motor.setIdleMode(rev.CANSparkMax.IdleMode.kCoast)
        self.motor.setSmartCurrentLimit(40)
        
        #self.controller.burnFlash()    

        self.clearFaults()

    def clearFaults(self):
        self.motor.clearFaults()
    
    def getSpeed(self):
        vel = -self.encoder.getVelocity()  # rpm
        return vel

    def setSpeed(self, speed):
        self.motor.set(speed)
        return None
        
class SwerveModule:
    angleMotor: SparkMaxTurning
    speedMotor: SparkMaxDriving

    def __init__(self):
        self.target_angle = 0
        self.meas_angle = 0
        self.target_speed = 0
        self.meas_speed = 0

        self.target_distance = 0
        self.tolerance = 0.001

        self.auto_lockout = 0
    
    def clearFaults(self):
        self.angleMotor.clearFaults()
        self.speedMotor.clearFaults()
        return False

    def getAngle(self):
        return self.meas_angle
    
    def getSpeed(self):
        return self.meas_speed

    def move(self, speed, angle):
        self.target_speed = speed
        self.target_angle = angle
        return False
    
    def execute(self):
        self.meas_speed = self.speedMotor.getSpeed()
        self.meas_angle = self.angleMotor.getAbsPosition()
        self.angleMotor.setAbsPosition(self.target_angle)
        self.speedMotor.setSpeed(self.target_speed) 

class SwerveDrive:
    DriveConfig: DriveConfig
    FrontLeft_SwerveModule: SwerveModule
    FrontRight_SwerveModule: SwerveModule
    RearLeft_SwerveModule: SwerveModule
    RearRight_SwerveModule: SwerveModule

    backLeft: SwerveModuleState
    backRight: SwerveModuleState
    frontLeft: SwerveModuleState
    frontRight: SwerveModuleState

    move_changed: bool = False

    _kinematics: SwerveDrive4Kinematics
    _odemetry: SwerveDrive4PoseEstimator

    
    @property
    def odemetry(self) -> SwerveDrive4PoseEstimator:
        return self._odemetry
    
    def __init__(self):
        self._kinematics = SwerveDrive4Kinematics(self.DriveConfig.frontLeftLocation,
                                                 self.DriveConfig.frontRightLocation,
                                                 self.DriveConfig.backLeftLocation,
                                                 self.DriveConfig.backRightLocation)
        
        # self._odemetry = SwerveDrive4PoseEstimator(self._kinematics,
        #                                            Rotation2d(math.radians(self._navx.getAngle())),
        #                                            module_positions, # type: ignore
        #                                            Pose2d(0,0,geom.Rotation2d(0)))
    
    # @property
    def isMoveChanged(self):
        return self.move_changed
    
    def clearFaults(self):
        self.RearLeft_SwerveModule.clearFaults()
        self.RearRight_SwerveModule.clearFaults()
        self.FrontLeft_SwerveModule.clearFaults()
        self.FrontRight_SwerveModule.clearFaults()
        return False

    def move(self, Lx, Ly, Rx, optimize=True): 

        speeds = ChassisSpeeds(Ly, Lx, Rx)

        self.frontLeft, self.frontRight, self.backLeft, self.backRight = self._kinematics.toSwerveModuleStates(speeds)

        if optimize:
            self.frontLeft = SwerveModuleState.optimize(self.frontLeft, Rotation2d(self.FrontLeft_SwerveModule.getAngle()))
            self.frontRight = SwerveModuleState.optimize(self.frontRight, Rotation2d(self.FrontRight_SwerveModule.getAngle()))
            self.backLeft = SwerveModuleState.optimize(self.backLeft, Rotation2d(self.RearLeft_SwerveModule.getAngle()))
            self.backRight = SwerveModuleState.optimize(self.backRight, Rotation2d(self.RearRight_SwerveModule.getAngle()))

        self.move_changed = True
        
        return False

    def execute(self):
        if self.isMoveChanged():

            self.FrontLeft_SwerveModule.move(self.frontLeft.speed,  self.frontLeft.angle)
            self.FrontRight_SwerveModule.move(self.frontRight.speed,  self.frontRight.angle)
            self.RearLeft_SwerveModule.move(self.backLeft.speed,  self.backLeft.angle)
            self.RearRight_SwerveModule.move(self.backRight.speed,  self.backRight.angle)

            self.move_changed = False
            
    

