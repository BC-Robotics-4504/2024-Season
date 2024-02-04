from wpimath.geometry import Translation2d
from wpimath.kinematics import SwerveDrive4Kinematics

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
        return math.hypot(self.chasis_length, self.chasis_width)

class SparkMaxTurning:
    """Swerve Drive SparkMax Class
    Custom class for configuring SparkMaxes used in Swerve Drive Drivetrain
    """
    
    # PID coefficients
    kP = 1
    kI = 0
    kD = 0
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
        self.motor.setInverted(inverted) #TODO: does this need to be removed?
                 
        self.encoder = self.motor.getAbsoluteEncoder(rev.SparkMaxAbsoluteEncoder.Type.kDutyCycle)
        self.controller = self.motor.getPIDController()
        self.controller.setFeedbackDevice(self.encoder)
        print(self.encoder, self.controller)
        
        self.encoder.setPositionConversionFactor(1)
        self.encoder.setVelocityConversionFactor(1)
        self.controller.setPositionPIDWrappingEnabled(True) #TODO: does this need to be removed?
        self.controller.setPositionPIDWrappingMinInput(0) #TODO: does this need to be removed?
        self.controller.setPositionPIDWrappingMaxInput(1) #TODO: does this need to be removed?
        # PID parameters
        self.controller.setP(self.kP)
        self.controller.setI(self.kI)
        self.controller.setD(self.kD)
        self.controller.setFF(self.kFF)
        self.controller.setOutputRange(self.kMinOutput, self.kMaxOutput)
        
        self.motor.setIdleMode(rev.CANSparkMax.IdleMode.kBrake)
        self.motor.setSmartCurrentLimit(25)
        
        #self.controller.burnFlash()    
        self.clearFaults()
    
    def clearFaults(self):
        self.motor.clearFaults()
    
    def setAbsPosition(self, position):
        # self.controller.setReference(position, rev.CANSparkMax.ControlType.kDutyCycle)
        self.controller.setReference(position, rev.CANSparkMax.ControlType.kPosition)
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
        self.target_speed = 0

        self.target_distance = 0
        self.tolerance = 0.001

        self.auto_lockout = 0
    
    def clearFaults(self):
        self.angleMotor.clearFaults()
        self.speedMotor.clearFaults()
        return False

    def getSpeedAngle(self):
        angle = self.angleMotor.getAbsPosition()
        speed = self.speedMotor.getSpeed()
        return speed, angle

    def move(self, speed, angle):
        self.target_speed = speed
        self.target_angle = angle
        return False
    
    def execute(self):
        # self.angleMotor.setAbsPosition(self.target_angle)
        # self.speedMotor.setSpeed(self.target_speed) 
        speed, angle = self.getSpeedAngle()
               


class SwerveDrive:
    DriveConfig: DriveConfig
    FrontLeft_SwerveModule: SwerveModule
    FrontRight_SwerveModule: SwerveModule
    RearLeft_SwerveModule: SwerveModule
    RearRight_SwerveModule: SwerveModule

    V1_speed: float = 0
    V1_angle: float = 0
    V2_speed: float = 0
    V2_angle: float = 0
    V3_speed: float = 0
    V3_angle: float = 0
    V4_speed: float = 0
    V4_angle: float = 0

    move_changed: bool = False

    # @property
    def isMoveChanged(self):
        return self.move_changed
    
    def clearFaults(self):
        self.RearLeft_SwerveModule.clearFaults()
        self.RearRight_SwerveModule.clearFaults()
        self.FrontLeft_SwerveModule.clearFaults()
        self.FrontRight_SwerveModule.clearFaults()
        return False

    def move(self, Lx, Ly, Rx, Ry, rateLimit = False): 
        """
        :param front_rear:
        :param right_left:
        :returns:
        """
        # strafe = Lx
        # fwd = Ly
        # rcw = Rx
        Vx0 = Lx
        Vy0 = Ly
        w0 = Rx

        A = Vx0 - w0 * self.DriveConfig.chasis_length/2
        B = Vx0 + w0 * self.DriveConfig.chasis_length/2
        C = Vy0 - w0 * self.DriveConfig.chasis_width/2
        D = Vy0 + w0 * self.DriveConfig.chasis_width/2

        # Wheel one
        self.V1_speed = math.hypot(B, C)
        self.V1_angle = math.atan2(C, B)

        # Wheel two
        self.V2_speed = math.hypot(B, D)
        self.V2_angle = math.atan2(D, B)

        # Wheel three
        self.V3_speed = math.hypot(A, D)
        self.V3_angle = math.atan2(D, A)

        # Wheel four
        self.V4_speed = math.hypot(A, C)
        self.V4_angle = math.atan2(C, A)

        self.move_changed = True

        # print('=================================')
        # print(f'{self.front_right_angle:0.3f}', 
        # f'{self.front_left_angle:0.3f}', 
        # f'{self.rear_left_angle:0.3f}', 
        # f'{self.rear_right_angle:0.3f}')
        return False

    def execute(self):
        if self.isMoveChanged():


            # self.FrontLeft_SwerveModule.move(self.V1_speed,  self.V1_angle)
            self.FrontLeft_SwerveModule.angleMotor.setAbsPosition(1.0)
            # self.FrontRight_SwerveModule.move(self.V2_speed,  self.V2_angle)
            # self.RearLeft_SwerveModule.move(self.V3_speed,  self.V3_angle)
            # self.RearRight_SwerveModule.move(self.V4_speed,  self.V4_angle)         
            #
            speed, angle = self.FrontLeft_SwerveModule.getSpeedAngle()
            print(f'{speed:0.3f}, {angle:0.3f}')   

            self.move_changed = False
            
       
            # print(f"Front Left Module - Angle: {self.front_left_angle}, Speed: {self.front_left_speed}")
            # print(f"Front Right Module - Angle: {self.front_right_angle}, Speed: {self.front_right_speed}")
            # print(f"Rear Left Module - Angle: {self.rear_left_angle}, Speed: {self.rear_left_speed}")
            # print(f"Rear Right Module - Angle: {self.rear_right_angle}, Speed: {self.rear_right_speed}")
            
    

