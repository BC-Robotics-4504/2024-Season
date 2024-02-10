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
    speed_clamp: float = 0.25

class SparkMaxTurning:
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
        self.SMcontroller.setReference(position-self.zOffset, rev.CANSparkMax.ControlType.kPosition)
        return False
    
    def getAbsPosition(self):
        rotation = self.encoder.getPosition()
        return rotation

class SparkMaxDriving:
    """Swerve Drive SparkMax Class
    Custom class for configuring SparkMaxes used in Swerve Drive Drivetrain
    """
    
    # PID coefficients
    kP = 1e-4
    kI = 1e-4
    kD = 1e-4
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
        
        self.encoder.setPositionConversionFactor(0.05077956125529683)
        self.encoder.setVelocityConversionFactor(0.0008463260209216138)
        
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

    def move(self, Lx, Ly, Rx): 

        A = -Lx + math.pi*Rx*self.DriveConfig.chasis_length
        B = -Lx - math.pi*Rx*self.DriveConfig.chasis_length
        C = Ly + math.pi*Rx*self.DriveConfig.chasis_width
        D = Ly - math.pi*Rx*self.DriveConfig.chasis_width

        self.frontLeft_angle = math.atan2(D, B)
        self.frontLeft_speed = math.hypot(D, B)

        self.rearLeft_angle = math.atan2(D, A)
        self.rearLeft_speed = math.hypot(D, A)

        self.rearRight_angle = math.atan2(C, A)
        self.rearRight_speed = math.hypot(C, A)

        self.frontRight_angle = math.atan2(C, B)
        self.frontRight_speed = math.hypot(C, B)

        self.move_changed = True
        
        return False

    def execute(self):
        if self.isMoveChanged():

            max_val = max([self.frontLeft_speed, self.frontRight_speed, self.rearLeft_speed, self.rearRight_speed])/self.DriveConfig.speed_clamp
            if abs(max_val) == 0:
                max_val = 1

            self.FrontLeft_SwerveModule.move(self.frontLeft_speed/max_val, self.frontLeft_angle)
            self.FrontRight_SwerveModule.move(self.frontRight_speed/max_val, self.frontRight_angle)
            self.RearLeft_SwerveModule.move(self.rearLeft_speed/max_val, self.rearLeft_angle)
            self.RearRight_SwerveModule.move(self.rearRight_speed/max_val, self.rearRight_angle)


            self.move_changed = False
            
    

