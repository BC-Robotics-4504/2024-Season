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

    # @property
    # def ratio(self):
    #     return math.hypot(self.chasis_length, self.chasis_width/2)

    # @property
    # def frontLeftLocation(self):
    #     return Translation2d(self.chasis_length/2, self.chasis_width/2)
    
    # @property
    # def frontRightLocation(self):
    #     return Translation2d(self.chasis_length/2, -self.chasis_width/2)
    
    # @property
    # def backLeftLocation(self):
    #     return Translation2d(-self.chasis_length/2, self.chasis_width/2)

    # @property
    # def backRightLocation(self):
    #     return Translation2d(-self.chasis_length/2, -self.chasis_width/2)  

class SparkMaxTurning:
    """Swerve Drive SparkMax Class
    Custom class for configuring SparkMaxes used in Swerve Drive Drivetrain
    """
    
    # PID coefficients
    kP = 1
    kI = 0
    kD = 0
    kIz = 0
    # kFF = 0.000156
    kFF = 0
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
        z_offset = 0
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

        self.motor = rev.CANSparkMax(self.canID, rev.CANSparkMax.MotorType.kBrushless)  
        self.motor.restoreFactoryDefaults()
        self.motor.setInverted(not inverted)
        self.motor.setIdleMode(rev.CANSparkMax.IdleMode.kBrake)
        self.motor.setSmartCurrentLimit(25)

        self.SMcontroller = self.motor.getPIDController()
        self.encoder = self.motor.getAbsoluteEncoder(rev.SparkMaxAbsoluteEncoder.Type.kDutyCycle)
        self.encoder.setInverted(inverted)
        self.encoder.setZeroOffset(z_offset/(2*math.pi))
        # self.encoder.setAverageDepth(1)
        # self.encoder.setZeroOffset(0)
        # self.encoder.setInverted(False)
        # self.encoder.setPositionConversionFactor(1.0)
        # self.encoder.setVelocityConversionFactor(1.0)
        self.SMcontroller.setFeedbackDevice(self.encoder)
        
        self.encoder.setPositionConversionFactor(1)
        self.encoder.setVelocityConversionFactor(1)
        self.SMcontroller.setPositionPIDWrappingEnabled(True) #TODO: does this need to be removed?
        self.SMcontroller.setPositionPIDWrappingMinInput(0) #TODO: does this need to be removed?
        self.SMcontroller.setPositionPIDWrappingMaxInput(1) #TODO: does this need to be removed?
        
        # PID parameters
        self.SMcontroller.setP(self.kP)
        self.SMcontroller.setI(self.kI)
        self.SMcontroller.setD(self.kD)
        self.SMcontroller.setIZone(self.kIz)
        self.SMcontroller.setFF(self.kFF)
        self.SMcontroller.setOutputRange(self.kMinOutput, self.kMaxOutput)

        # # Smart Motion Parameters
        # self.SMcontroller.setSmartMotionMaxVelocity(self.maxVel, self.smartMotionSlot)
        # self.SMcontroller.setSmartMotionMinOutputVelocity(self.minVel, self.smartMotionSlot)
        # self.SMcontroller.setSmartMotionMaxAccel(self.maxAcc, self.smartMotionSlot)
        # self.SMcontroller.setSmartMotionAllowedClosedLoopError(self.allowedErr, self.smartMotionSlot)
        
        #self.controller.burnFlash()    
        self.clearFaults()
    
    def clearFaults(self):
        self.motor.clearFaults()
    
    def setAbsPosition(self, position):
        self.SMcontroller.setReference(position, rev.CANSparkMax.ControlType.kPosition)
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

    frontLeft_angle = 0
    frontLeft_speed = 0
    frontRight_angle = 0
    frontRight_speed = 0
    rearLeft_angle = 0
    rearLeft_speed = 0
    rearRight_angle = 0
    rearRight_speed = 0

    move_changed: bool = False

    # _kinematics: SwerveDrive4Kinematics
    # _odemetry: SwerveDrive4PoseEstimator

    
    @property
    def odemetry(self) -> SwerveDrive4PoseEstimator:
        return self._odemetry
    
    def __init__(self):
        pass
    #     self._kinematics = SwerveDrive4Kinematics(self.DriveConfig.frontLeftLocation,
    #                                              self.DriveConfig.frontRightLocation,
    #                                              self.DriveConfig.backLeftLocation,
    #                                              self.DriveConfig.backRightLocation)

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

        A = Lx - math.pi*Rx*self.DriveConfig.chasis_length
        B = Lx + math.pi*Rx*self.DriveConfig.chasis_length
        C = Ly - math.pi*Rx*self.DriveConfig.chasis_width
        D = Ly + math.pi*Rx*self.DriveConfig.chasis_width

        self.frontRight_angle = math.atan2(C, B)
        self.frontRight_speed = math.hypot(C, B)

        self.frontLeft_angle = math.atan2(D, B)
        self.frontLeft_speed = math.hypot(D, B)

        self.rearLeft_angle = math.atan2(D, A)
        self.rearLeft_speed = math.hypot(D, A)

        self.rearRight_angle = math.atan2(C, A)
        self.rearRight_speed = math.hypot(C, A)

        # speeds = ChassisSpeeds(Ly, Lx, Rx)

        # self.frontLeft, self.frontRight, self.backLeft, self.backRight = self._kinematics.toSwerveModuleStates(speeds)

        # if optimize:
        #     self.frontLeft = SwerveModuleState.optimize(self.frontLeft, Rotation2d(self.FrontLeft_SwerveModule.getAngle()))
        #     self.frontRight = SwerveModuleState.optimize(self.frontRight, Rotation2d(self.FrontRight_SwerveModule.getAngle()))
        #     self.backLeft = SwerveModuleState.optimize(self.backLeft, Rotation2d(self.RearLeft_SwerveModule.getAngle()))
        #     self.backRight = SwerveModuleState.optimize(self.backRight, Rotation2d(self.RearRight_SwerveModule.getAngle()))
        # self.frontLeft_speed = Lx
        # self.frontLeft_angle = Rx
        self.move_changed = True
        
        return False

    def execute(self):
        if self.isMoveChanged():

            self.FrontLeft_SwerveModule.move(self.frontLeft_speed,  self.frontLeft_angle)
            self.FrontRight_SwerveModule.move(self.frontRight_speed,  self.frontRight_angle)
            self.RearLeft_SwerveModule.move(self.rearLeft_speed,  self.rearLeft_angle)
            self.RearRight_SwerveModule.move(self.rearRight_speed,  self.rearRight_angle)

            self.move_changed = False
            
    

